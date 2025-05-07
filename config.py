import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GRAPHHOPPER_API_KEY = os.getenv("GRAPHHOPPER_API_KEY")
