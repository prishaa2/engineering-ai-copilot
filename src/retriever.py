import chromadb

client = chromadb.PersistentClient(path="data/vector_db")

collection = client.get_or_create_collection(
    name="engineering_documents"
)

def store_chunks(chunks):
    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            documents=[chunk["text"]],
            embeddings=[chunk["embedding"]],
            metadatas=[
                {
                    "source": chunk["source"]
                }
            ]
        )