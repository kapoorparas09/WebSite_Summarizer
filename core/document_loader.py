from pypdf import PdfReader
from docx import Document
from config import MAX_INPUT_CHARS

def load_txt(file):
    text = file.read().decode("utf-8")
    return text[:MAX_INPUT_CHARS]

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "
    return text[:MAX_INPUT_CHARS]

def load_docx(file):
    doc = Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text[:MAX_INPUT_CHARS]

def load_document(file):
    if file.name.endswith(".txt") or file.name.endswith(".md"):
        return load_txt(file)

    elif file.name.endswith(".pdf"):
        return load_pdf(file)

    elif file.name.endswith(".docx"):
        return load_docx(file)

    else:
        raise ValueError("Unsupported file format")