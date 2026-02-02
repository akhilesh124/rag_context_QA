
# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma

# loader = TextLoader("data/company_policy.txt")
# documents = loader.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# docs = splitter.split_documents(documents)

# vectordb = Chroma.from_documents(
#     documents=docs,
#     embedding=OpenAIEmbeddings(),
#     persist_directory="./chroma_db"
# )

# vectordb.persist()
# print("✅ Company policy ingested successfully")



from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Load document
def story_embeding():
    loader = TextLoader("data/story1.txt",encoding="utf-8")
    documents = loader.load()
    print("documents")
    # 2. Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    # 3. Create embedding model (NO OpenAI)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # 4. Store in Chroma (local)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    # 5. Persist DB
    vectordb.persist()
    print("✅ Company policy ingested successfully (Local Embeddings)")
    return "data injected successfully"
    


