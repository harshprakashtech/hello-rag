import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Google genai client
client = genai.Client(api_key=GEMINI_API_KEY)

# Interact with the model
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Explain how AI works in a few words"
)

print(interaction.output_text)
