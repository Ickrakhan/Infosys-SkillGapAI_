# import streamlit as st
# import pandas as pd

# def download_csv(data):
#     df = pd.DataFrame(
#         data["skill_scores"].items(),
#         columns=["Skill", "Score"]
#     )

#     csv = df.to_csv(index=False).encode("utf-8")

#     st.download_button(
#         "⬇ Download CSV",
#         csv,
#         "skill_gap_report.csv",
#         "text/csv"
#     )

import pandas as pd
import streamlit as st


def download_csv(data):
    rows = []

    for skill in data["all_skills"]:
        rows.append({
            "Skill": skill,
            "Status": "Matched" if skill in data["matched_skills"] else "Missing"
        })

    df = pd.DataFrame(rows)

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv,
        file_name="skill_gap_report.csv",
        mime="text/csv"
    )

