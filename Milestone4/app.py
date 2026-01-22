import streamlit as st
import PyPDF2
import docx

from dashboard.metrics import analyze_skills
from dashboard.charts import show_visuals
from reports.csv_report import download_csv
from reports.pdf_report import download_pdf


# ---------------- FILE READERS ----------------
def read_txt(file):
    return file.read().decode("utf-8", errors="ignore")


def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def read_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])


def extract_text(file):
    if file.type == "text/plain":
        return read_txt(file)
    elif file.type == "application/pdf":
        return read_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return read_docx(file)
    return ""


# ---------------- SIMPLE SKILL EXTRACTOR ----------------
def extract_skills(text):
    skill_bank = [
        "python", "java", "sql", "machine learning", "data analysis",
        "excel", "communication", "html", "css", "javascript",
        "power bi", "tableau", "numpy", "pandas"
    ]

    text = text.lower()
    return list({skill for skill in skill_bank if skill in text})


# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="Skill Gap Analysis", layout="wide")

st.title("📊 Skill Gap Analysis Dashboard")
st.write("Upload a **Resume** and **Job Description** to analyze skill matching.")

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "docx", "txt"]
    )

with col2:
    jd_file = st.file_uploader(
        "📝 Upload Job Description",
        type=["pdf", "docx", "txt"]
    )

# ---------------- PROCESSING ----------------
if resume_file and jd_file:
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    data = analyze_skills(resume_skills, jd_skills)

    # ---------------- SUMMARY METRICS ----------------
    st.subheader("📌 Match Summary")

    m1, m2, m3 = st.columns(3)
    m1.metric("Match Percentage", f"{data['match_percentage']}%")
    m2.metric("Matched Skills", len(data["matched_skills"]))
    m3.metric("Missing Skills", len(data["missing_skills"]))

    if data["match_level"] == "High Match":
        st.success(f"✅ Overall Result: {data['match_level']}")
    elif data["match_level"] == "Partial Match":
        st.warning(f"⚠️ Overall Result: {data['match_level']}")
    else:
        st.error(f"❌ Overall Result: {data['match_level']}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ---------------- VISUALS ----------------
    show_visuals(data)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ---------------- DOWNLOAD REPORTS ----------------
    st.subheader("📥 Download Reports")
    download_csv(data)
    download_pdf(data)

else:
    st.info("⬆️ Please upload both Resume and Job Description to continue.")
