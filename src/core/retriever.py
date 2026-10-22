
import re


def retrieve_documents(vectordb, query, k=5):
    query = query.strip()

    if not query:
        return []

    # Normal vector retrieval
    vector_docs = vectordb.similarity_search(
        query,
        k=k
    )

    # For explicit week queries, also search by exact section wording.
    match = re.search(
        r"\bweek\s+(\d+)\b",
        query,
        re.IGNORECASE
    )

    if not match:
        return vector_docs

    week_number = match.group(1)

    # Search using the expected heading phrase.
    keyword_docs = vectordb.similarity_search(
        f"Week {week_number}:",
        k=k
    )

    # Merge results, keeping unique chunks.
    combined = []
    seen = set()

    for doc in keyword_docs + vector_docs:
        key = (
            doc.metadata.get("source", ""),
            doc.metadata.get("page", ""),
            doc.page_content
        )

        if key not in seen:
            seen.add(key)
            combined.append(doc)

    # Prefer chunks that explicitly mention the requested week.
    heading_pattern = re.compile(
        rf"\bweek\s+{week_number}\s*:",
        re.IGNORECASE
    )

    combined.sort(
        key=lambda doc: bool(
            heading_pattern.search(doc.page_content)
        ),
        reverse=True
    )

    return combined[:k]
