import streamlit as st
import spacy
import pandas as pd
import matplotlib.pyplot as plt

# ================= Page Config =================
st.set_page_config(page_title="Milestone 2: Skill Extraction using NLP", layout="wide")

# ================= Load Model =================
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# ================= Skill Lists =================
TECH_SKILLS = [
    "Python", "Machine Learning", "TensorFlow", "SQL", "Statistics",
    "Data Visualization", "Power BI", "Tableau", "AWS", "Azure", "GCP"
]

SOFT_SKILLS = [
    "Communication", "Team Leadership", "Problem Solving"
]

# ================= Skill Extraction =================
def extract_skills(text, skill_list):
    found = []
    text = text.lower()
    for skill in skill_list:
        if skill.lower() in text:
            found.append(skill)
    return found

# ================= Header (Exact Style) =================
st.markdown("""
<style>
.skill-tag {
    display: inline-block;
    padding: 6px 12px;
    margin: 5px;
    border-radius: 20px;
    font-size: 13px;
    background-color: #e6f4f1;
    color: #0f766e;
    font-weight: 600;
}
.section-card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}
</style>

<div style="background-color:#2f8f83;padding:18px;border-radius:8px">
    <h2 style="color:white;margin-bottom:5px">Milestone 2: Skill Extraction using NLP Module (Weeks 3–4)</h2>
    <p style="color:white">spaCy & BERT-based pipelines • Technical & Soft Skills • Structured Skill Display</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ================= Layout =================
left, right = st.columns([1.3, 1])

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Skill Extraction Interface")

    resume_text = st.text_area("Resume Text", height=180)
    jd_text = st.text_area("Job Description Text", height=180)

    if st.button("Extract Skills"):
        res_tech = extract_skills(resume_text, TECH_SKILLS)
        res_soft = extract_skills(resume_text, SOFT_SKILLS)
        jd_tech = extract_skills(jd_text, TECH_SKILLS)
        jd_soft = extract_skills(jd_text, SOFT_SKILLS)

        st.markdown("#### Resume Skills")
        for s in res_tech:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)
        for s in res_soft:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

        st.markdown("#### Job Description Skills")
        for s in jd_tech:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)
        for s in jd_soft:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Skill Distribution")

    if 'res_tech' in locals():
        tech_count = len(res_tech) + len(jd_tech)
        soft_count = len(res_soft) + len(jd_soft)

        fig, ax = plt.subplots()
        ax.pie([tech_count, soft_count], labels=["Technical Skills", "Soft Skills"], autopct="%1.0f%%")
        st.pyplot(fig)

        c1, c2, c3 = st.columns(3)
        c1.metric("Technical Skills", tech_count)
        c2.metric("Soft Skills", soft_count)
        c3.metric("Total Skills", tech_count + soft_count)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= Detailed Skills =================
st.write("")
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("Detailed Skills")

if 'res_tech' in locals():
    df = pd.DataFrame({
        "Skill": list(set(res_tech + res_soft + jd_tech + jd_soft)),
        "Category": ["Technical" if s in TECH_SKILLS else "Soft" for s in set(res_tech + res_soft + jd_tech + jd_soft)]
    })
    st.dataframe(df, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.caption("Infosys Springboard • Skill Gap Analysis • Milestone 2")
