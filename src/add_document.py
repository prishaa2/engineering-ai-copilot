from pypdf import PdfReader
from src.ingest import chunk_documents
from src.embeddings import create_embedding
from src.retriever import add_chunks


def add_document(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    document = [{
        "filename": pdf_path.name,
        "text": text
    }]

    chunks = chunk_documents(document)

    for chunk in chunks:
        chunk["embedding"] = create_embedding(chunk["text"])

    add_chunks(chunks)