import subprocess
from pathlib import Path

def convert_to_wav(input_path: Path) -> Path:
    """
    Converts the downloaded audio file (usually .mp4) into a .wav file using ffmpeg.
    Returns the path to the converted .wav file.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path = input_path.with_suffix(".wav")  # Replace extension with .wav

    command = [
        "ffmpeg",
        "-y",                 # overwrite output if exists
        "-i", str(input_path), # input file
        "-ac", "1",           # mono audio (better for transcription)
        "-ar", "16000",       # 16kHz sample rate (required by many models)
        str(output_path)
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not output_path.exists():
        raise RuntimeError("ffmpeg failed to convert the audio file.")

    return output_path