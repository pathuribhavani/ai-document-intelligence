from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os

from app.pdf_processor import extract_text_from_pdf
from app.chunker import chunk_text
from app.search import DocumentSearch
from app.ai_service import generate_answer


app = FastAPI(title="AI Document Intelligence Platform")

uploaded_file_path = None


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/cors-test")
def cors_test():
    return {
        "message": "CORS test works"
    }


class SearchRequest(BaseModel):
    question: str


@app.post("/documents/upload")
def upload_document(file: UploadFile = File(...)):

    global uploaded_file_path

    upload_folder = "uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    uploaded_file_path = file_path

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }


@app.post("/documents/ask")
def ask_document(request: SearchRequest):

    if uploaded_file_path is None:
        return {
            "error": "Please upload a document first."
        }

    file_path = uploaded_file_path

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    search_engine = DocumentSearch(chunks)

    results = search_engine.search(
        request.question,
        top_k=3
    )

    context = "\n\n".join(
        result["chunk"]
        for result in results
    )

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": results
    }


@app.post("/documents/search")
def search_document(request: SearchRequest):

    if uploaded_file_path is None:
        return {
            "error": "Please upload a document first."
        }

    file_path = uploaded_file_path

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