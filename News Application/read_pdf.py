from pathlib import Path
import sys

path = Path("06-052 Capstone Project – News Application.pdf")
print("exists", path.exists())
try:
    import PyPDF2

    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        print("pages", len(reader.pages))
        for i, page in enumerate(reader.pages[:5]):
            print(f"--- PAGE {i+1} ---")
            text = page.extract_text() or ""
            print(text[:1200])
except Exception as e:
    print("ERROR", type(e).__name__, e)
    sys.exit(1)
