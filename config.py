# config.py

# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Replace with your actual Hugging Face model ID
# HF_MODEL_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# # Add your Hugging Face access token in a .env file like: HUGGINGFACE_API_KEY=your_token_here
# HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# HEADERS = {
#     "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
#     "Content-Type": "application/json"
# }

# API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
# config.py
# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment or .env file.")
