# import streamlit as st

# def show_metrics(data):
#     col1, col2, col3 = st.columns(3)

#     col1.metric("Overall Match", f"{data['overall_match']}%")
#     col2.metric("Matched Skills", len(data["matched_skills"]))
#     col3.metric("Missing Skills", len(data["missing_skills"]))

#     st.markdown(f"### Match Level: **{data['match_level']}**")


def analyze_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched_skills = sorted(resume_set & jd_set)
    missing_skills = sorted(jd_set - resume_set)

    match_percentage = round((len(matched_skills) / len(jd_set)) * 100, 2) if jd_set else 0

    if match_percentage >= 70:
        match_level = "High Match"
    elif match_percentage >= 40:
        match_level = "Partial Match"
    else:
        match_level = "Low Match"

    return {
        "all_skills": sorted(jd_set),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage,
        "match_level": match_level
    }
