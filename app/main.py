from fastapi import FastAPI

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