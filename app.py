import streamlit as st
from core.scraper import extract_text_from_url
from core.summarizer import summarize
from config import DEFAULT_MODEL

st.set_page_config(page_title="WebIntel LLM", layout="wide")

# Force clean white UI
st.markdown("""
<style>
    body {
        background-color: white;
    }
    .stTextArea textarea {
        background-color: white !important;
        color: black !important;
        font-family: Arial;
    }
</style>
""", unsafe_allow_html=True)

st.title("WEBINTEL LLM – WEBSITE REPORT GENERATOR")

url = st.text_input("Enter Website URL")
pages = st.slider("Summary Length (Pages)", 1, 10, 2)
model_name = st.selectbox("Model", [DEFAULT_MODEL, "llama3"])

if st.button("Generate Report"):
    if url:
        with st.spinner("Scraping website..."):
            text = extract_text_from_url(url)

        with st.spinner("Generating report..."):
            summary = summarize(text, pages, model_name)

        st.success("Report Generated Successfully")

        st.subheader("Generated Report")
        st.text_area("", summary, height=600)

        st.download_button(
            label="Download as TXT",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter a valid URL.")