# import streamlit as st
# from fpdf import FPDF

# def clean_text(text):
#     """
#     Remove emojis / non-latin characters for PDF
#     """
#     return text.encode("latin-1", "ignore").decode("latin-1")

# def download_pdf(data):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, "Skill Gap Analysis Report", ln=True)
#     pdf.ln(5)

#     # Clean text before writing to PDF
#     match_level = clean_text(data["match_level"])

#     pdf.cell(200, 10, f"Overall Match: {data['overall_match']}%", ln=True)
#     pdf.cell(200, 10, f"Match Level: {match_level}", ln=True)
#     pdf.ln(5)

#     pdf.cell(200, 10, "Matched Skills:", ln=True)
#     for skill in data["matched_skills"]:
#         pdf.cell(200, 10, f"- {clean_text(skill)}", ln=True)

#     pdf.ln(5)
#     pdf.cell(200, 10, "Missing Skills:", ln=True)
#     for skill in data["missing_skills"]:
#         pdf.cell(200, 10, f"- {clean_text(skill)}", ln=True)

#     pdf_output = pdf.output(dest="S").encode("latin-1")

#     st.download_button(
#         "⬇ Download PDF",
#         pdf_output,
#         "skill_gap_report.pdf",
#         "application/pdf"
#     )


from fpdf import FPDF
import streamlit as st


def download_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Skill Gap Analysis Report", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, f"Match Percentage: {data['match_percentage']}%", ln=True)
    pdf.cell(0, 10, f"Overall Result: {data['match_level']}", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, "Matched Skills:", ln=True)
    for skill in data["matched_skills"]:
        pdf.cell(0, 8, f"- {skill}", ln=True)

    pdf.ln(3)
    pdf.cell(0, 10, "Missing Skills:", ln=True)
    for skill in data["missing_skills"]:
        pdf.cell(0, 8, f"- {skill}", ln=True)

    pdf_output = pdf.output(dest="S").encode("latin-1", errors="ignore")

    st.download_button(
        label="⬇️ Download PDF Report",
        data=pdf_output,
        file_name="skill_gap_report.pdf",
        mime="application/pdf"
    )
