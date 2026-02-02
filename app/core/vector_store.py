from langchain_community.vectorstores import Chroma
from app.config.settings import VECTOR_DB_PATH
from langchain_openai import OpenAIEmbeddings

from langchain_community.embeddings import HuggingFaceEmbeddings

# embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# vector = embed_model.embed_query("Hello world")


# def get_vector_store():
#     embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # vector = embed_model.embed_query("Hello world")
    # print("gjhfihfjhdfjfjh",vector)

def get_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    return vectordb

# def get_vector_store():
#     embeddings = OpenAIEmbeddings()
#     vectordb = Chroma(
#         persist_directory=VECTOR_DB_PATH,
#         embedding_function=embeddings
#     )
#     return vectordb