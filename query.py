from src.core.embeddings import get_embedding_model
from src.core.vectorstore import load_vectorstore
from src.core.retriever import retrieve_documents

embedding_model = get_embedding_model()

vectordb = load_vectorstore(
    embedding_model
)

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    docs = retrieve_documents(
        vectordb,
        question,
        k=5
    )

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(docs, 1):

        print(f"\nChunk {i}")
        print("-" * 50)

        print(doc.page_content[:300])