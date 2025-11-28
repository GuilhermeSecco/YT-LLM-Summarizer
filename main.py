from pathlib import Path
from src.downloader import download_audio
from src.converter import convert_to_wav
from src.summarizer import transcribe_audio, generate_summary
import argparse
from dotenv import load_dotenv
load_dotenv()

def run_pipeline(url: str) -> Path:
    """
    Full summarization pipeline:
    1. Download audio
    2. Convert to WAV
    3. Transcribe audio
    4. Generate summary
    5. Save summary to summaries/<video_id>.md
    """

    print("[1/5] Downloading audio...")
    audio_mp4 = download_audio(url)

    print("[2/5] Converting audio to WAV...")
    audio_wav = convert_to_wav(audio_mp4)

    print("[3/5] Transcribing audio...")
    transcript = transcribe_audio(audio_wav)

    print("[4/5] Generating summary with LLM...")
    summary_text = generate_summary(transcript)

    # Create output folder
    summaries_dir = Path("summaries")
    summaries_dir.mkdir(exist_ok=True)

    video_id = audio_mp4.stem  # filename without extension
    output_file = summaries_dir / f"{video_id}.md"

    print("[5/5] Saving summary...")
    output_file.write_text(summary_text, encoding="utf-8")

    print(f"\nSummary saved to: {output_file}")
    return output_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube LLM Summarizer")
    parser.add_argument("--url", type=str, required=True, help="YouTube video URL")

    args = parser.parse_args()
    run_pipeline(args.url)