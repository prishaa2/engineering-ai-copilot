from src.ingest import load_documents, chunk_documents
from src.embeddings import create_embedding
from src.retriever import collection, store_chunks


def initialize_database():
    """
    Build the vector database automatically if it is empty.
    """

    if collection.count() > 0:
        print("Vector database already initialized.")
        return

    print("Initializing vector database...")

    documents = load_documents()

    chunks = chunk_documents(documents)

    for chunk in chunks:
        chunk["embedding"] = create_embedding(chunk["text"])

    store_chunks(chunks)

    print(f"Indexed {len(chunks)} chunks.")