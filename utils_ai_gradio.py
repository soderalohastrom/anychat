import gradio as gr
import google.generativeai as genai

def create_gemini_chat(model_name: str, **kwargs):
    model = genai.GenerativeModel(model_name.replace('gemini:', ''))
    
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(
                [],
                elem_id="chatbot",
                bubble_full_width=False,
                avatar_images=(None, None),
                height=400 if not kwargs.get('fill_height') else None,
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

def get_app(
    models: list[str],
    default_model: str,
    dropdown_label: str = "Select Model",
    choices: list[str] = None,
    **kwargs,
) -> gr.Blocks:
    display_choices = choices if choices is not None else models
    
    def update_model(new_model: str) -> list[gr.Column]:
        if choices is not None:
            idx = display_choices.index(new_model)
            new_model = models[idx]
        return [gr.Column(visible=model_name == new_model) for model_name in models]

    with gr.Blocks(fill_height=True) as demo:
        model = gr.Dropdown(
            label=dropdown_label, 
            choices=display_choices,
            value=choices[models.index(default_model)] if choices else default_model
        )

        columns = []
        for model_name in models:
            with gr.Column(visible=model_name == default_model) as column:
                if model_name.startswith('gemini:'):
                    create_gemini_chat(model_name, **kwargs)
                else:
                    from ai_gradio.providers import registry
                    gr.load(name=model_name, src=registry, **kwargs)
                columns.append(column)

        model.change(
            fn=update_model,
            inputs=model,
            outputs=columns,
            api_name=False,
            queue=False,
        )

    for fn in demo.fns.values():
        fn.api_name = False

    return demo