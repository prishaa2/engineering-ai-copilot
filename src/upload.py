from pathlib import Path

DOCUMENT_FOLDER = Path("data/documents")


def save_uploaded_files(files):
    DOCUMENT_FOLDER.mkdir(parents=True, exist_ok=True)

    saved = []

    for file in files:
        destination = DOCUMENT_FOLDER / file.name

        with open(destination, "wb") as f:
            f.write(file.getbuffer())

        saved.append(destination)

    return saved