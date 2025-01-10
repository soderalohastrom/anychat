import ai_gradio
from utils_ai_gradio import get_app

# Import Together AI provider
from ai_gradio.providers.together_gradio import registry as together_registry

# Use Gemma models from Together AI
GEMINI_MODELS_FULL = [
    'google/gemma-2-27b-it',
    'google/gemma-2-9b-it',
    'google/gemma-2b-it'
]

# Create display names without the path
GEMINI_MODELS_DISPLAY = [
    k.split('/')[-1].replace('-it', '')  # Clean up display names
    for k in GEMINI_MODELS_FULL
]

# Create and launch the interface using get_app utility
demo = get_app(
    models=GEMINI_MODELS_FULL,
    default_model=GEMINI_MODELS_FULL[0],  # Use the largest model as default
    dropdown_label="Select Gemma Model",
    src=together_registry
)

