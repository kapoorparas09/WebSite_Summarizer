def build_summary_prompt(text: str, target_words: int):
    return f"""
Generate a clean professional report of approximately {target_words} words.

STRICT FORMATTING RULES:
- DO NOT use markdown symbols like **, *, #, or ---
- Use only plain text
- Use uppercase section headings
- Leave one blank line between sections
- Use hyphen (-) for bullet points only
- Keep formatting minimal and professional

STRUCTURE:

TITLE

INTRODUCTION

COMPANY OVERVIEW

KEY INSIGHTS

INDUSTRIES

SUCCESS STORIES

CONCLUSION

Website Content:
{text}
"""