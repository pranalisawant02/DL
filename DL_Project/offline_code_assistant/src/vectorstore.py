from langchain_community.vectorstores import FAISS

def create_vectorstore(texts, metadata, embeddings):
    vectorstore = FAISS.from_texts(
        texts,
        embeddings,
        metadatas=metadata
    )
    return vectorstore