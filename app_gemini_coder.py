from utils_ai_gradio import get_app

# Define available Gemini/Gemma models
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
    default_model=GEMINI_MODELS_FULL[0],
    dropdown_label="Select Gemini Model",
    choices=GEMINI_MODELS_DISPLAY,
    fill_height=True,
    coder=True,
)

