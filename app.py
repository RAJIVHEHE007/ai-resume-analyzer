import streamlit as st
from utils import extract_text_from_pdf, analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("🚀 AI Resume Analyzer")
job_description=st.text_area("paste job Description(optional)")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing your resume..."):
            text = extract_text_from_pdf(uploaded_file)

            if text.strip() == "":
                st.error("Could not extract text from PDF")
            else:
                result = analyze_resume(text + "\n job Description:\n + job Description")
                st.subheader("📊 Analysis Result")
                st.write(result)
