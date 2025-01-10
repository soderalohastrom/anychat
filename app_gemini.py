import ai_gradio
from utils_ai_gradio import get_app

# Get available Gemma models from registry
GEMINI_MODELS_FULL = [
    k for k in ai_gradio.registry.keys()
    if 'gemma' in k.lower()
]

if not GEMINI_MODELS_FULL:
    # Fallback to hardcoded models if none found in registry
    GEMINI_MODELS_FULL = [
        'together:google/gemma-2-27b-it',
        'together:google/gemma-2-9b-it',
        'together:google/gemma-2b-it'
    ]

# Create display names without the prefix
GEMINI_MODELS_DISPLAY = [
    k.split('/')[-1].replace('-it', '')  # Clean up display names
    for k in GEMINI_MODELS_FULL
]

# Create and launch the interface using get_app utility
demo = get_app(
    models=GEMINI_MODELS_FULL,
    default_model=GEMINI_MODELS_FULL[0],  # Use the largest model as default
    dropdown_label="Select Gemma Model",
    src=ai_gradio.registry
)

