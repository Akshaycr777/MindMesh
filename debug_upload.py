
import os
from pathlib import Path
from rag import read_file_text

uploads_dir = Path("uploads")
files = list(uploads_dir.glob("*.pdf"))
if not files:
    print("No PDFs found in uploads folder.")
else:
    latest_file = max(files, key=os.path.getctime)
    print(f"Latest PDF: {latest_file}")
    try:
        text = read_file_text(latest_file)
        print(f"Text length: {len(text)}")
        if not text.strip():
            print("ERROR: Text is completely empty or whitespace.")
        else:
            print(f"Snippet: {text[:100]}")
    except Exception as e:
        print(f"Exception: {repr(e)}")

