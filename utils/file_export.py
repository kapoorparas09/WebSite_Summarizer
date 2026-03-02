def export_txt(summary: str, filename="summary.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)