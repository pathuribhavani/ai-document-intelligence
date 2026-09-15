# AI Document Intelligence Platform

An AI-powered document question-answering platform that allows users to upload documents and ask questions using natural language.

## Features

- Upload PDF documents
- Extract text from documents
- Split documents into manageable chunks
- Generate local AI embeddings
- Store embeddings in ChromaDB
- Perform similarity search
- Ask questions about uploaded documents
- Generate answers using a local LLM with Ollama
- Display relevant document sources
- React frontend
- FastAPI backend
- No OpenAI API key required

## Architecture

React
   |
   v
FastAPI
   |
   +--> Document Upload
   |
   +--> PDF Text Extraction
   |
   +--> Text Chunking
   |
   +--> Sentence Transformers
   |
   +--> ChromaDB
   |
   +--> Similarity Search
   |
   +--> Ollama
   |
   v
AI Answer + Sources

## Technologies

### Backend
- Python
- FastAPI
- Sentence Transformers
- ChromaDB
- PyPDF
- Scikit-learn

### Frontend
- React
- Vite
- JavaScript

### AI
- Hugging Face Sentence Transformers
- Ollama
- Llama 3.2

## Running the Backend

```bash
cd ai-document-intelligence
source venv/bin/activate
uvicorn app.main:app --reload