from pdf_processor import extract_text_from_pdf
from chunker import chunk_text
from search import DocumentSearch
from ai_service import generate_answer

file_path = "uploads/python.pdf"


text = extract_text_from_pdf(file_path)

chunks = chunk_text(text)

search_engine = DocumentSearch(chunks)


question = input("Ask a question about your document: ")

results = search_engine.search(question, top_k=3)


context = "\n\n".join(
    result["chunk"]
    for result in results
)


answer = generate_answer(question, context)


print("\nAI Answer:\n")
print(answer)


print("\nSources:\n")

for result in results:
    print("Score:", result["score"])
    print(result["chunk"])
    print("-" * 50)