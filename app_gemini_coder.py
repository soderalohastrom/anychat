import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize the model
model = genai.GenerativeModel('gemini-pro-code')

# Create the chat interface
with gr.Blocks(fill_height=True) as demo:
    chatbot = gr.Chatbot(
        [],
        elem_id="chatbot",
        bubble_full_width=False,
        avatar_images=(None, None),
        height=600,
        show_copy_button=True,
        type="messages",  # Use new messages format
    )
    txt = gr.Textbox(
        scale=4,
        show_label=False,
        placeholder="Enter text and press enter",
        container=False,
    )

    def respond(message, chat_history):
        if not message:
            return "", chat_history
        
        # Add user message
        chat_history.append({"role": "user", "content": message})
        
        # Generate response
        response = model.generate_content(message)
        
        # Add assistant response
        if response.text:
            chat_history.append({"role": "assistant", "content": response.text})
        else:
            chat_history.append({"role": "assistant", "content": "Failed to generate response"})
        
        return "", chat_history

    txt.submit(respond, [txt, chatbot], [txt, chatbot])