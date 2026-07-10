from langchain_chroma import Chroma

PERSIST_DIR = "vectordb"

def create_vectorstore(chunks, embedding_model):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=PERSIST_DIR,
        collection_metadata={
            "hnsw:space": "cosine"
        }
    )

    return vectordb


def load_vectorstore(embedding_model):

    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedding_model
    )