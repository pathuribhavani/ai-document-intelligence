from pdf_processor import extract_text_from_pdf
from chunker import chunk_text
from embeddings import create_embeddings


file_path = "uploads/python.pdf"

text = extract_text_from_pdf(file_path)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Total characters:", len(text))
print("Total chunks:", len(chunks))
print("Embedding count:", embeddings.shape[0])
print("Embedding size:", embeddings.shape[1])