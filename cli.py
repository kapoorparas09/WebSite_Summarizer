import argparse
from core.scraper import extract_text_from_url
from core.summarizer import summarize
from utils.file_export import export_txt

def main():
    parser = argparse.ArgumentParser(description="Website Summarizer CLI")
    parser.add_argument("--url", required=True)
    parser.add_argument("--pages", type=int, default=2)

    args = parser.parse_args()

    print("Fetching website...")
    text = extract_text_from_url(args.url)

    print("Generating summary...")
    summary = summarize(text, args.pages)

    export_txt(summary)

    print("\nSummary saved as summary.txt\n")
    print(summary)

if __name__ == "__main__":
    main()