import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")  # No fallback
VECTOR_DB_PATH = "./chroma_db"

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set! Check your .env file or environment variables.")