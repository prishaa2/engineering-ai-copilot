from src.ingest import load_documents

docs = load_documents()

for doc in docs:
    if doc["filename"] == "MATERIAL SCIENCE.pdf":

        text = doc["text"]

        start = 0

        while True:

            idx = text.lower().find("modulus", start)

            if idx == -1:
                break

            print("=" * 80)
            print(text[max(0, idx-300):idx+700])

            start = idx + 1