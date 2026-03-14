import gradio as gr
from audiocraft.models import MusicGen

from band_loader import load_band_profile
from prompt_engine import build_prompt


print("Loading MusicGen model...")
model = MusicGen.get_pretrained("facebook/musicgen-medium")
model.set_generation_params(duration=30)


def generate_music(band_name, theme, tempo):

    band = load_band_profile(band_name)

    prompt = build_prompt(band, theme, tempo)

    print("\nPrompt used:")
    print(prompt)

    audio = model.generate([prompt])

    # MusicGen returns tensors, convert to playable format
    wav = audio[0].cpu().numpy()

    return (32000, wav)


bands_available = ["mirrorspine"]


demo = gr.Interface(
    fn=generate_music,
    inputs=[
        gr.Dropdown(bands_available, label="Band"),
        gr.Textbox(label="Song Theme", placeholder="haunted orchard at dusk"),
        gr.Slider(60, 120, value=85, step=1, label="Tempo BPM")
    ],
    outputs=gr.Audio(label="Generated Song"),
    title="Signal Forge Studio",
    description="AI Music Studio powered by Audiocraft"
)

demo.launch()
