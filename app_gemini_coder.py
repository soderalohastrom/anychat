import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils_ai_gradio import get_app

# Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Define available models
GEMINI_MODELS_FULL = ['gemini:gemini-pro-code']
GEMINI_MODELS_DISPLAY = ['gemini-pro-code']

# Create and launch the interface using get_app utility
demo = get_app(
    models=GEMINI_MODELS_FULL,  # Use the full names with prefix
    default_model=GEMINI_MODELS_FULL[0],  # Use first model as default
    dropdown_label="Select Gemini Model",
    choices=GEMINI_MODELS_DISPLAY,  # Display names without prefix
    fill_height=True,
    coder=True
)