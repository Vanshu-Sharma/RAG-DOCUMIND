from src.core.memory import get_chat_history
from src.core.embeddings import get_embedding_model
from src.core.vectorstore import load_vectorstore
from src.core.retriever import retrieve_documents
from src.core.llm import generate_answer
print("Loading Embeddings...")
embedding_model = get_embedding_model()
print("Loading Vector DB...")
vectordb = load_vectorstore(
    embedding_model
)
print("Vector DB Ready")

def rag_pipeline(question):

    docs = retrieve_documents(
        vectordb,
        question,
        k=5
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    history = get_chat_history()
    history_text = "\n".join(
    [
        f"{msg['role']}: {msg['content']}"
        for msg in history
    ]
    )

    answer = generate_answer(
     question,
     context,
     history_text
     )

    return answer, docs