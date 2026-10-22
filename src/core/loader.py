
from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    if not documents:
        raise ValueError(
            "No text could be extracted from this PDF."
        )

    total_chars = sum(
        len(doc.page_content) for doc in documents
    )

    print(f"Pages extracted: {len(documents)}")
    print(f"Total characters extracted: {total_chars}")

    return documents
