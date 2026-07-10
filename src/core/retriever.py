def retrieve_documents(vectordb, query, k=5):

    docs = vectordb.similarity_search(
        query,
        k=k
    )

    return docs