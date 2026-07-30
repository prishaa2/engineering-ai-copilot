from src.ingest import load_documents, chunk_documents
from src.embeddings import create_embedding
from src.retriever import collection, store_chunks


def initialize_database():

    if collection.count() > 0:
        print("Vector database already initialized.")
        return

    print("Initializing vector database...")

    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    for i, chunk in enumerate(chunks):
        if i % 100 == 0:
            print(f"Embedding {i}/{len(chunks)}")
        chunk["embedding"] = create_embedding(chunk["text"])

    print("Finished embeddings.")

    store_chunks(chunks)

    print("Initialization complete.")