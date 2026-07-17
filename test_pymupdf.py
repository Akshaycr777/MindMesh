import fitz; doc=fitz.open("uploads/9e131f89-c3da-4bb7-937d-87c4f81a1652_case_study_assignment.pdf"); text = "".join(page.get_text() for page in doc); print("Text length with pymupdf:", len(text))
