from src.core.embeddings import get_embedding_model
from src.core.vectorstore import load_vectorstore
from src.core.retriever import retrieve_documents
from src.core.llm import generate_answer

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
    print(f"\nDocuments Retrieved: {len(docs)}")

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(docs, 1):

         print(f"\nChunk {i}")
         print("-" * 50)

         print(doc.page_content[:300])

    answer = generate_answer(
        question,
        context
    )

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for doc in docs:

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        print(
            f"Page {page}"
        )