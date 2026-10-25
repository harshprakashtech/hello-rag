from config import init_model
from ingest import ingest_data


# Run engine (Main function)
def run_engine():
    # Initialize AI model
    client = init_model()

    # Ingest data from file
    data = ingest_data("data/pagepoint_cafe.txt")

    print(data)
