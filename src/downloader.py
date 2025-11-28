import re
from pathlib import Path
from pytubefix import YouTube

def extract_video_id(url: str) -> str:
    """
    Extracts the YouTube video ID from common URL formats using simple string operations.
    Supports:
    - Standard links
    - Short links
    - Shorts links
    - Raw video ID
    """

    # Case: user passes only the raw video ID
    if len(url) == 11 and "/" not in url:
        return url

    # Standard: https://www.youtube.com/watch?v=VIDEO_ID
    if "v=" in url:
        return url.split("v=")[1][:11]

    # Short link: https://youtu.be/VIDEO_ID
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1][:11]

    # Shorts link: https://www.youtube.com/shorts/VIDEO_ID
    if "youtube.com/shorts/" in url:
        return url.split("youtube.com/shorts/")[1][:11]

    raise ValueError(f"Could not extract video ID from URL: {url}")

def download_audio(url: str) -> Path:
    """
    Downloads the audio stream of a YouTube video and saves it into the /temp directory.
    Returns the path to the downloaded audio file.
    """
    video_id = extract_video_id(url)

    # Create temp directory if it doesn't exist
    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)

    # Build output path: temp/<video_id>.mp4
    output_path = temp_dir / f"{video_id}.mp4"

    # Download audio
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if audio_stream is None:
        raise RuntimeError("No audio stream available for this video.")

    audio_stream.download(output_path=str(output_path))

    return output_path