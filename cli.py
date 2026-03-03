import argparse
from core.scraper import extract_text_from_url
from core.document_loader import load_document
from core.summarizer import summarize
from utils.file_export import export_txt

def main():
    parser = argparse.ArgumentParser(description="WebIntel CLI")

    parser.add_argument("--url", help="Website URL")
    parser.add_argument("--file", help="Document file path")
    parser.add_argument("--pages", type=int, default=2)

    args = parser.parse_args()

    if args.url:
        text = extract_text_from_url(args.url)

    elif args.file:
        with open(args.file, "rb") as f:
            text = load_document(f)

    else:
        print("Provide either --url or --file")
        return

    summary = summarize(text, args.pages)
    export_txt(summary)

    print("Summary saved as summary.txt")

if __name__ == "__main__":
    main()