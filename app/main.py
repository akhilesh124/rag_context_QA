from fastapi import FastAPI
from app.controllers.rag_controller import router as rag_router
from dotenv import load_dotenv
import os
app = FastAPI(
    title="Company Policy RAG API",
    version="1.0.0"
)
load_dotenv() 
app.include_router(rag_router)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("Using API key:", OPENAI_API_KEY[:8], "...")
@app.get("/")
def health_check():
    return {"status": "RAG API running"}
