import gradio as gr
from crew_config import create_crew
from gradio.themes.ocean import Ocean

def optimize_gig(profile_text):
    crew = create_crew(profile_text)
    result = crew.kickoff()
    return result

# Custom CSS to constrain layout width
custom_css = """
.container {
    max-width: 900px;
    margin: auto;
}
"""

with gr.Blocks(theme=Ocean(), css=custom_css) as demo:
    with gr.Column(elem_classes=["container"]):
        gr.Markdown(
            """
            <h1 style='text-align: center; color: #4EA8DE;'>🧠 Freelancer Gig Optimizer</h1>
            <p style='text-align: center; font-size: 16px;'>Paste your raw freelancer profile. Let the AI turn it into an optimized gig for Upwork/Fiverr.</p>
            """
        )

        profile_input = gr.Textbox(
            lines=8,
            label="📝 Your Raw Freelancer Profile",
            placeholder="Paste your raw profile here...",
            show_copy_button=True
        )

        optimize_button = gr.Button("🚀 Optimize My Gig")

        optimized_output = gr.Textbox(
            label="🎯 Optimized Gig",
            lines=10,
            interactive=False,
            placeholder="Your output will be displayed here...",
            show_copy_button=True
        )

        optimize_button.click(
            fn=optimize_gig,
            inputs=profile_input,
            outputs=optimized_output
        )

if __name__ == "__main__":
    demo.launch()
