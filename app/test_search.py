from pdf_processor import extract_text_from_pdf
from chunker import chunk_text
from search import DocumentSearch


file_path = "uploads/python.pdf"

text = extract_text_from_pdf(file_path)

chunks = chunk_text(text)

search_engine = DocumentSearch(chunks)

query = "shipment product database"

results = search_engine.search(query)

print("\nSearch Results:\n")

for result in results:
    print("Score:", result["score"])
    print("Text:", result["chunk"])
    print("-" * 50)