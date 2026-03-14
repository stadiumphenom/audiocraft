def build_prompt(band_profile: dict, theme: str, tempo: int) -> str:
    """
    Build a structured MusicGen prompt using the band profile.
    """

    prompt = f"""
    genre: {band_profile['genre']}
    tempo: {tempo} BPM
    tuning: {band_profile['tuning']}
    guitars: {band_profile['guitar_style']}
    rhythm: {band_profile['rhythm_section']}
    vocals: {band_profile['vocal_style']}
    production: {band_profile['production']}
    theme: {theme}
    """

    return prompt.strip()
