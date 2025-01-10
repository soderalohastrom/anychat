from ai_gradio.providers import registry
from utils_ai_gradio import get_app

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

# Create and launch the interface using get_app utility
demo = get_app(
    models=GEMINI_MODELS_FULL,  # Use the full names with prefix
    default_model=GEMINI_MODELS_FULL[-1],
    dropdown_label="Select Gemini Model",
    choices=GEMINI_MODELS_DISPLAY,  # Display names without prefix
    src=registry,
    fill_height=True,
    coder=True,
)