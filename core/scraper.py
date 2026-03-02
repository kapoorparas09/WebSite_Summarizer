import requests
from bs4 import BeautifulSoup
from config import MAX_INPUT_CHARS

def extract_text_from_url(url: str):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    text = soup.get_text(separator=" ")
    text = " ".join(text.split())

    return text[:MAX_INPUT_CHARS]