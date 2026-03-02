from config import WORDS_PER_PAGE, DEFAULT_MODEL
from models.client import get_client
from models.prompts import build_summary_prompt

client = get_client()

def summarize(text: str, pages: int, model_name: str = DEFAULT_MODEL):
    target_words = pages * WORDS_PER_PAGE
    prompt = build_summary_prompt(text, target_words)

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()