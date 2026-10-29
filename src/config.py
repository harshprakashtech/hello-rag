import os

from google import genai


# Config and initialize AI model (Gemini)
def init_client():
    # Load Gemini API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Initialize google genai client
    client = genai.Client(api_key=GEMINI_API_KEY)

    return client
