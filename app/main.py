from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.pdf_processor import extract_text_from_pdf
from app.chunker import chunk_text
from app.search import DocumentSearch
from pydantic import BaseModel

app = FastAPI(title="AI Document Intelligence Platform")
class SearchRequest(BaseModel):
    question: str


@app.post("/documents/search")
def search_document(request: SearchRequest):

    file_path = "uploads/python.pdf"

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    search_engine = DocumentSearch(chunks)

    results = search_engine.search(request.question)

    return {
        "question": request.question,
        "results": results
    }

@app.get("/")
def home():
    return {
        "message": "AI Document Intelligence Platform is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.post("/documents/upload")
def upload_document(file: UploadFile = File(...)):

    upload_folder = "uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }