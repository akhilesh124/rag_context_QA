from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from app.core.vector_store import get_vector_store


def get_rag_answer(question: str) -> str:
    # 1. Get vector store
    vectordb = get_vector_store()

    # similarity search
    docs = vectordb.similarity_search(question, k=3)

    # combine retrieved text
    context = "\n\n".join(doc.page_content for doc in docs)

    return context
    # 2. Create retriever
    # retriever = vectordb.as_retriever(
    #     search_kwargs={"k": 3}
    # )
    # return retriever
    # # 3. LLM
    # llm = ChatOpenAI(
    #     model="gpt-3.5-turbo",
    #     temperature=0
    # )

    # # 4. Prompt
    # prompt = ChatPromptTemplate.from_template(
    #     """
    #     You are an assistant answering questions based ONLY on the context below.
    #     If the answer is not present in the context, say "Answer not found in policy".

    #     Context:
    #     {context}

    #     Question:
    #     {question}
    #     """
    # )

    # # 5. RAG Chain (LCEL)
    # chain = (
    #     {"context": retriever, "question": RunnablePassthrough()}
    #     | prompt
    #     | llm
    #     | StrOutputParser()
    # )

    # # 6. Invoke chain
    # return chain.invoke(question)
