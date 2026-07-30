import chromadb
from src.embeddings import create_embedding

client = chromadb.PersistentClient(path="data/vector_db")

collection = client.get_or_create_collection(
    name="engineering_documents"
)

def store_chunks(chunks):
    global collection

    client.delete_collection("engineering_documents")

    collection = client.get_or_create_collection(
        name="engineering_documents"
    )

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            documents=[chunk["text"]],
            embeddings=[chunk["embedding"]],
            metadatas=[{"source": chunk["source"]}]
        )

    print(f"Stored {len(chunks)} chunks.")

def add_chunks(chunks):
    existing = collection.count()

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(existing + i)],
            documents=[chunk["text"]],
            embeddings=[chunk["embedding"]],
            metadatas=[{"source": chunk["source"]}]
        )

    print(f"Added {len(chunks)} chunks.")

def retrieve_chunks(query, k=10):
    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results