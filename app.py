import streamlit as st
from core.scraper import extract_text_from_url
from core.document_loader import load_document
from core.summarizer import summarize
from config import DEFAULT_MODEL

st.set_page_config(page_title="WebSite Summarizer and Document Reader", layout="wide")

# Clean white UI
st.markdown("""
<style>
    body { background-color: white; }
    .stTextArea textarea {
        background-color: white !important;
        color: black !important;
        font-family: Arial;
    }
</style>
""", unsafe_allow_html=True)

st.title("WEBSITE & DOCUMENT REPORT GENERATOR")

# Source selection
source_type = st.radio(
    "Select Source Type",
    ["Website", "Document"]
)

pages = st.slider("Summary Length (Pages)", 1, 10, 2)
model_name = st.selectbox("Model", [DEFAULT_MODEL, "llama3"])

text = None

if source_type == "Website":
    url = st.text_input("Enter Website URL")
    if st.button("Generate Report"):
        if url:
            with st.spinner("Scraping website..."):
                text = extract_text_from_url(url)

        else:
            st.warning("Please enter a valid URL.")

elif source_type == "Document":
    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["txt", "pdf", "docx", "md"]
    )

    if st.button("Generate Report"):
        if uploaded_file:
            with st.spinner("Reading document..."):
                text = load_document(uploaded_file)

        else:
            st.warning("Please upload a document.")

# Generate summary if text exists
if text:
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