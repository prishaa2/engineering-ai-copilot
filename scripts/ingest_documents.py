from src.ingest import load_documents, chunk_documents
from src.embeddings import create_embedding
from src.retriever import store_chunks


def main():
    print("=" * 50)
    print("Engineering AI Copilot")
    print("Building Vector Database")
    print("=" * 50)

    documents = load_documents()

    print(f"Loaded {len(documents)} document(s).")

    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    for i, chunk in enumerate(chunks):
        if i % 100 == 0:
            print(f"Embedding chunk {i}/{len(chunks)}")

        chunk["embedding"] = create_embedding(chunk["text"])

    print("Saving to ChromaDB...")

    store_chunks(chunks)

    print("\nVector database successfully built!")


if __name__ == "__main__":
    main()