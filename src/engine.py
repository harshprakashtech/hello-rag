from embed import get_embeddings
from ingest import ingest_data


# Run engine (Main function)
def run_engine():
    # Ingest data from file
    data = ingest_data("data/pagepoint_cafe.txt")

    # Generate embeddings
    embeddings = get_embeddings(data, model="gemini-embedding-001")