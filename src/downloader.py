import re
from pytubefix import YouTube
from pathlib import Path

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
    video_id = extract_video_id(url)

    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)

    yt = YouTube(url)
    title = yt.title

    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream is None:
        raise RuntimeError("No audio stream found.")

    # Download to temp directory with default pytubefix filename
    downloaded = Path(audio_stream.download(output_path=str(temp_dir)))

    # Extract extension
    ext = downloaded.suffix  # .m4a, .mp4, .webm

    # Our final desired path
    final = temp_dir / f"{video_id}{ext}"

    # Rename real file to our expected name
    if downloaded != final:
        downloaded.rename(final)

    return final, title