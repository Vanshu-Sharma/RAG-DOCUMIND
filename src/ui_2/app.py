import os
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# Make sure the project root (the folder containing the `src` package) is on
# sys.path, regardless of which subfolder this file lives in. Streamlit only
# adds this file's own directory to sys.path, so `import src...` otherwise fails.
_current = Path(__file__).resolve()
for _parent in _current.parents:
    if (_parent / "src").is_dir():
        sys.path.insert(0, str(_parent))
        break

from src.core.loader import load_pdf
from src.core.chunker import get_text_splitter
from src.core.embeddings import get_embedding_model
from src.core.vectorstore import create_vectorstore, load_vectorstore
from src.core.retriever import retrieve_documents
from src.core.llm import generate_answer

load_dotenv()

st.set_page_config(page_title="RAG Assistant", page_icon="📄", layout="wide")

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


@st.cache_resource(show_spinner=False)
def load_embedding_model():
    return get_embedding_model()


def get_vectordb(embedding_model):
    """Load an existing vector DB from disk once per session, if present."""
    if "vectordb" not in st.session_state:
        try:
            st.session_state.vectordb = load_vectorstore(embedding_model)
        except Exception:
            st.session_state.vectordb = None
    return st.session_state.vectordb


def ingest_pdf(uploaded_file, embedding_model):
    pdf_path = os.path.join(DATA_DIR, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    documents = load_pdf(pdf_path)
    splitter = get_text_splitter()
    chunks = splitter.split_documents(documents)
    vectordb = create_vectorstore(chunks, embedding_model)

    st.session_state.vectordb = vectordb
    return len(chunks)


def render_sources(docs, key_prefix):
    with st.expander(f"Sources & retrieved chunks ({len(docs)})"):
        for i, doc in enumerate(docs, 1):
            page = doc.metadata.get("page", "Unknown")
            st.markdown(f"**Chunk {i} — Page {page}**")
            st.text(doc.page_content[:500])
            st.divider()


# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("📄 RAG Assistant")
    st.caption("Upload a PDF, build the index, then ask questions.")

    st.divider()
    st.subheader("Document")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Ingest PDF", use_container_width=True, type="primary"):
            embedding_model = load_embedding_model()
            with st.spinner("Loading, chunking, and embedding..."):
                try:
                    n_chunks = ingest_pdf(uploaded_file, embedding_model)
                    st.success(f"Indexed {n_chunks} chunks from {uploaded_file.name}")
                except Exception as e:
                    st.error(f"Ingestion failed: {e}")

    st.divider()
    st.subheader("Retrieval settings")
    k = st.slider("Chunks to retrieve (k)", min_value=1, max_value=10, value=5)
    show_chunks = st.checkbox("Show retrieved chunks", value=True)

    st.divider()
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------- Main ----------------
st.header("Ask your document")

embedding_model = load_embedding_model()
vectordb = get_vectordb(embedding_model)

if vectordb is None:
    st.info("No index found yet. Upload a PDF in the sidebar and click **Ingest PDF** to get started.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("docs"):
            render_sources(message["docs"], key_prefix=message["content"][:20])

question = st.chat_input("Ask a question about your document...")

if question:
    if vectordb is None:
        st.warning("Please ingest a PDF first.")
    else:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Retrieving and generating answer..."):
                docs = retrieve_documents(vectordb, question, k=k)
                context = "\n\n".join(doc.page_content for doc in docs)
                answer = generate_answer(question, context)

            st.markdown(answer)

            if show_chunks and docs:
                render_sources(docs, key_prefix="latest")

        st.session_state.messages.append(
            {"role": "assistant", "content": answer, "docs": docs}
        )
