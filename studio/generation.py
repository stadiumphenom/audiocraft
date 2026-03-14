import argparse
from audiocraft.models import MusicGen

from band_loader import load_band_profile
from prompt_engine import build_prompt


def generate_song(band_name: str, theme: str, tempo: int):

    band = load_band_profile(band_name)

    prompt = build_prompt(band, theme, tempo)

    print("Using prompt:")
    print(prompt)

    model = MusicGen.get_pretrained("facebook/musicgen-medium")

    model.set_generation_params(
        duration=30
    )

    audio = model.generate([prompt])

    return audio


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--band", required=True)
    parser.add_argument("--theme", required=True)
    parser.add_argument("--tempo", type=int, required=True)

    args = parser.parse_args()

    generate_song(args.band, args.theme, args.tempo)
