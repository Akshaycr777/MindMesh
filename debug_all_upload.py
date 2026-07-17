
import os
from pathlib import Path
from rag import read_file_text

uploads_dir = Path("uploads")
files = list(uploads_dir.glob("*.pdf"))
for f in files:
    try:
        text = read_file_text(f)
        if text.strip():
            print(f"File: {f.name} -> SUCCESS (len: {len(text)})")
        else:
            print(f"File: {f.name} -> EMPTY TEXT")
    except Exception as e:
        print(f"File: {f.name} -> ERROR: {repr(e)}")

