from src.ingest import load_documents, chunk_documents
from src.embeddings import create_embedding
from src.retriever import store_chunks

documents = load_documents()

chunks = chunk_documents(documents)

for chunk in chunks:
    chunk["embedding"] = create_embedding(chunk["text"])

store_chunks(chunks)

print(f"Stored {len(chunks)} chunks in ChromaDB.")