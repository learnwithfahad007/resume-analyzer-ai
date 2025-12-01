import streamlit as st
from utils import extract_text_from_file, extract_skills, ats_score


st.title("AI Resume Analyzer")

uploaded = st.file_uploader("Upload resume (PDF or TXT)")
job_text = st.text_area(
    "Paste target job description skills (comma-separated)")


if st.button("Analyze"):
    if uploaded is None:
        st.warning("Please upload a resume")
    else:
        # Extract text
        text = extract_text_from_file(uploaded)

        # Extract resume skills
        skills = extract_skills(text)
        st.subheader("Extracted Skills")
        st.write(skills)

        # Target job skills
        target_skills = [s.strip() for s in job_text.split(",") if s.strip()]

        # ATS score
        score = ats_score(skills, target_skills)
        st.subheader("ATS Score (Match %)")
        st.write(f"{score}%")

        # Missing skills
        if target_skills:
            missing = [s for s in target_skills if s not in skills]
            st.subheader("Suggested Skills to Add")
            st.write(missing if missing else "None — great match!")
