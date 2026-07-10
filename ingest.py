from src.core.loader import load_pdf
from src.core.chunker import get_text_splitter
from src.core.embeddings import get_embedding_model
from src.core.vectorstore import create_vectorstore

PDF_PATH = "data/CPH.pdf"

print("Loading PDF...")

documents = load_pdf(PDF_PATH)

print("Chunking...")

splitter = get_text_splitter()

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

print("Loading Embedding Model...")

embedding_model = get_embedding_model()

print("Creating Vector DB...")

vectordb = create_vectorstore(
    chunks,
    embedding_model
)

print("Done!")