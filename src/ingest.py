from pathlib import Path
from pypdf import PdfReader

DOCUMENT_FOLDER = Path("data/documents")


def load_documents():
    pdf_files = list(DOCUMENT_FOLDER.glob("*.pdf"))

    if not pdf_files:
        print("No PDFs found.")
        return []

    documents = []

    for pdf in pdf_files:
        reader = PdfReader(pdf)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        documents.append({
            "filename": pdf.name,
            "text": text,
        })

    return documents

def chunk_documents(documents, chunk_size=500, overlap=100):
    chunks = []

    for doc in documents:
        text = doc["text"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "source": doc["filename"]
            })

            start += chunk_size - overlap

    return chunks