import gradio as gr
from crew_config import create_crew
from gradio.themes.ocean import Ocean

def optimize_gig(profile_text):
    crew = create_crew(profile_text)
    result = crew.kickoff()
    return result

with gr.Blocks(theme=Ocean()) as demo:
    gr.Markdown(
        """
        <h1 style='text-align: center; color: #4EA8DE;'>🧠 Freelancer Gig Optimizer</h1>
        <p style='text-align: center; font-size: 16px;'>Paste your raw freelancer profile. Let the AI turn it into an optimized gig for Upwork/Fiverr.</p>
        """
    )

    inp = gr.Textbox(
        lines=8,
        label="📝 Your Raw Freelancer Profile",
        placeholder="Paste your raw profile here...",
        show_copy_button=True
    )

    create_btn = gr.Button("🚀 Optimize My Gig")

    out = gr.Textbox(
        label="🎯 Optimized Gig",
        lines=10,
        interactive=False,
        placeholder="Your output will be displayed here...",
        show_copy_button=True
    )

    create_btn.click(fn=optimize_gig, inputs=inp, outputs=out)

demo.launch()
