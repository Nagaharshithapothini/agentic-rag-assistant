from app.vector_store import create_vector_store

vector_store = create_vector_store()


def retrieve_context(query: str):

    documents = vector_store.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context
