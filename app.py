from app_claude import demo as demo_claude
from app_cohere import demo as demo_cohere
from app_experimental import demo as demo_experimental
from app_fireworks import demo as demo_fireworks
from app_huggingface import demo as demo_huggingface
from app_meta import demo as demo_meta
from app_mistral import demo as demo_mistral
from app_nvidia import demo as demo_nvidia
from app_omini import demo as demo_omini
from app_paligemma import demo as demo_paligemma
from app_perplexity import demo as demo_perplexity
from app_replicate import demo as demo_replicate
from app_sambanova import demo as demo_sambanova
from app_showui import demo as demo_showui
from app_together import demo as demo_together
from app_qwen import demo as demo_qwen
from app_crew import demo as demo_crew
from app_compare import demo as demo_compare
from app_smolagents import demo as demo_smolagents
from app_gemini import demo as demo_gemini
from dotenv import load_dotenv
import gradio as gr
import os

# Load environment variables from .env file
load_dotenv()

# Create mapping of providers to their demos
PROVIDERS = {
    "SmolAgents": demo_smolagents,
    "Compare": demo_compare,
    "Qwen": demo_qwen,
    "Gemini": demo_gemini,
    "CrewAI": demo_crew,
    "Cohere": demo_cohere,
    "SambaNova": demo_sambanova,
    "OminiControl": demo_omini,
    "Fireworks": demo_fireworks,
    "Together": demo_together,
    "Meta Llama": demo_meta,
    "Paligemma": demo_paligemma,
    "Replicate": demo_replicate,
    "Huggingface": demo_huggingface,
    "ShowUI": demo_showui,
    "Claude": demo_claude,
    "Perplexity": demo_perplexity,
    "Experimental": demo_experimental,
    "Mistral": demo_mistral,
    "NVIDIA": demo_nvidia,
}

# Import Gemini Coder demo separately since it has a different implementation
from app_gemini_coder import demo as demo_gemini_coder

# Create the combined interface
with gr.Blocks() as demo:
    gr.Markdown("# AnyChat Demo")
    
    with gr.Tabs():
        with gr.Tab("Gemini Coder"):
            demo_gemini_coder.render()
        
        with gr.Tab("Other Models"):
            from utils import get_app
            other_models = get_app(
                models=list(PROVIDERS.keys()),
                default_model="Gemini",
                src=PROVIDERS,
                dropdown_label="Select Provider"
            )
            other_models.render()

if __name__ == "__main__":
    demo.queue(api_open=False).launch(
        server_name="0.0.0.0",  # Make server externally visible
        server_port=7860,       # Default Gradio port
        share=False,            # Don't use Gradio's sharing service
        show_api=False
    )