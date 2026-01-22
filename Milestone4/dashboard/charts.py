import pandas as pd
import plotly.express as px
import streamlit as st


def show_visuals(data):
    # ---------- TABLE ----------
    rows = []
    for skill in data["all_skills"]:
        rows.append({
            "Skill": skill.upper(),
            "Status": "Matched" if skill in data["matched_skills"] else "Missing"
        })

    df = pd.DataFrame(rows)

    st.subheader("📋 Skill-wise Status")
    st.dataframe(df, use_container_width=True)

    # ---------- BAR CHART ----------
    chart_df = pd.DataFrame({
        "Category": ["Matched Skills", "Missing Skills"],
        "Count": [len(data["matched_skills"]), len(data["missing_skills"])]
    })

    fig = px.bar(
        chart_df,
        x="Count",
        y="Category",
        orientation="h",
        text="Count",
        title="Skill Gap Summary"
    )

    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
