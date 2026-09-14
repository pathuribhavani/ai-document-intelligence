from pdf_processor import extract_text_from_pdf
from chunker import chunk_text


file_path = "uploads/python.pdf"

text = extract_text_from_pdf(file_path)

chunks = chunk_text(text)

print("Total characters:", len(text))
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\n--- Chunk", i + 1, "---")
    print(chunk)