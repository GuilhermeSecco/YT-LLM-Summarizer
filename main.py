from pathlib import Path
from src.downloader import download_audio
from src.converter import convert_to_wav
from src.summarizer import transcribe_audio, generate_summary
import argparse
from dotenv import load_dotenv
load_dotenv()

def sanitize_filename(title: str) -> str:
    return "".join(c for c in title if c.isalnum() or c in " .-_").strip()

def run_pipeline(url: str) -> Path:
    """
    Full summarization pipeline:
    1. Download audio
    2. Convert to WAV
    3. Transcribe audio
    4. Generate summary
    5. Save summary to summaries/<video_id>.md
    """

    print("[1/6] Downloading audio...")
    audio_mp4, video_title = download_audio(url)

    print("[2/6] Converting audio to WAV...")
    audio_wav = convert_to_wav(audio_mp4)

    print("[3/6] Transcribing audio...")
    transcript = transcribe_audio(audio_wav)

    print("[4/6] Generating summary with LLM...")
    summary_text = generate_summary(transcript)

    # Create output folder
    summaries_dir = Path("summaries")
    summaries_dir.mkdir(exist_ok=True)

    # Set file name as video title
    safe_title = sanitize_filename(video_title)
    output_file = summaries_dir / f"{safe_title}.md"

    print("[5/6] Saving summary...")
    output_file.write_text(summary_text, encoding="utf-8")
    print(f"\nSummary saved to: {output_file}")

    # Cleanup temp files
    print("[6/6] Cleaning temporary files...")
    import shutil
    temp_dir = Path("temp")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
        temp_dir.mkdir(exist_ok=True)

    print("All Done!")
    return output_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube LLM Summarizer")
    parser.add_argument("--url", type=str, help="YouTube video URL")

    args = parser.parse_args()

    # If URL was provided via CLI → use it
    if args.url:
        run_pipeline(args.url)
    else:
        # Fallback for running via PyCharm "play" button
        print("No URL provided via --url")
        url = input("Enter YouTube URL: ").strip()
        run_pipeline(url)