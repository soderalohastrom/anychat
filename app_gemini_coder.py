import os
import google.generativeai as genai
from dotenv import load_dotenv
from ai_gradio.providers import registry

# Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize Gemini models
GEMINI_MODELS = {
    'gemini:gemini-pro-code': genai.GenerativeModel('gemini-pro-code'),
}

# Register models in the registry
for model_name, model in GEMINI_MODELS.items():
    registry[model_name] = model

# Get the Gemini models but keep their full names for loading
GEMINI_MODELS_FULL = [
    k for k in registry.keys()
    if k.startswith('gemini:')
]

# Create display names without the prefix
GEMINI_MODELS_DISPLAY = [
    k.replace('gemini:', '')
    for k in GEMINI_MODELS_FULL
]

# Ensure there are models available
if not GEMINI_MODELS_FULL:
    GEMINI_MODELS_FULL = ['gemini:gemini-pro-code']
    GEMINI_MODELS_DISPLAY = ['gemini-pro-code']

# Import get_app after model registration
from utils_ai_gradio import get_app

# Create and launch the interface using get_app utility
demo = get_app(
    models=GEMINI_MODELS_FULL,  # Use the full names with prefix
    default_model=GEMINI_MODELS_FULL[0],  # Use first model as default
    dropdown_label="Select Gemini Model",
    choices=GEMINI_MODELS_DISPLAY,  # Display names without prefix
    src=registry,
    fill_height=True,
    coder=True
)