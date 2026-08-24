from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


def create_vector_store():

    documents = [
        Document(
            page_content="RAG combines information retrieval with language models.",
            metadata={"source": "rag_document"}
        ),
        Document(
            page_content="LangGraph can be used to build stateful AI agent workflows.",
            metadata={"source": "langgraph_document"}
        ),
        Document(
            page_content="Vector databases store embeddings for semantic search.",
            metadata={"source": "vector_database_document"}
        )
    ]

    embeddings = OpenAIEmbeddings()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="enterprise_docs"
    )

    return vector_store
