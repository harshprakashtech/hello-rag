# Read data from file
def read_file(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        text = f.read()

    return text


# Clean provided text data
def clean_data(text_data: str) -> list[str]:
    parts = []

    for part in text_data.split("\n\n"):
        if part.strip():
            parts.append(part.strip())

    return parts


# Ingest data (Main function)
def ingest_data(file_path: str) -> list[str]:
    text_data = read_file(file_path)
    cleaned_data = clean_data(text_data)

    return cleaned_data
