from src.ingest import load_documents, chunk_documents

print("=" * 50)
print("Engineering AI Copilot")
print("Document Ingestion")
print("=" * 50)

documents = load_documents()

print(f"\nLoaded {len(documents)} PDF(s).")

chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks.")