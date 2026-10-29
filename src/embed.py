from config import init_client


def get_embeddings(content: list[str], model: str) -> dict[int, list[float]]:
    client = init_client()

    # Generate embedding using the specified model
    result = client.models.embed_content(model=model, contents=content)

    embeddings = {}

    for i, embedding in enumerate(result.embeddings):
        embeddings[i] = embedding.values

    return embeddings
