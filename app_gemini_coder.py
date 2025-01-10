from utils_ai_gradio import get_app

# Define specific Gemini models
GEMINI_MODELS_FULL = [
    'gemini:gemini-2.0-flash-exp',
    'gemini:gemini-2.0-flash-thinking-exp-1219'
]

# Create display names without the prefix
GEMINI_MODELS_DISPLAY = [
    k.replace('gemini:', '')
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

