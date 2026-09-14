from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI(title="AI Document Intelligence Platform")


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