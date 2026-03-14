import json
import os


def load_band_profile(band_name: str) -> dict:
    """
    Load a band profile from the bands directory.
    """
    path = os.path.join("bands", band_name, "band_profile.json")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Band profile not found: {path}")

    with open(path, "r") as f:
        return json.load(f)
