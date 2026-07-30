from src.ingest import load_documents, chunk_documents
from src.embeddings import create_embedding
from src.retriever import collection, store_chunks


def initialize_database():

    print("Step 1")
    count = collection.count()
    print(f"Step 2 - Count = {count}")

    if count > 0:
        print("Already initialized.")
        return

    print("Step 3 - Loading documents")
    documents = load_documents()

    print(f"Loaded {len(documents)} docs")

    print("Step 4 - Chunking")
    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Step 5 - Creating embeddings")

    for i, chunk in enumerate(chunks):
        if i % 100 == 0:
            print(f"Embedding {i}/{len(chunks)}")

        chunk["embedding"] = create_embedding(chunk["text"])

    print("Step 6 - Storing")

    store_chunks(chunks)

    print("DONE")