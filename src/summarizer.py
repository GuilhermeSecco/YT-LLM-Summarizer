from pathlib import Path
import whisper
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def transcribe_audio(audio_path: Path) -> str:
    """
    Transcribes audio using Whisper (local, offline, free).
    Returns transcript text as string.
    """
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    model = whisper.load_model("base")
    result = model.transcribe(str(audio_path))

    return result["text"]


def generate_summary(text: str) -> str:
    """
    Generates a structured summary using Gemini Flash (free tier).
    Format:
    - Short Summary
    - Key Points
    - Important Insights
    """

    prompt = f"""
You are an AI assistant that summarizes YouTube transcript content in a clean,
structured, professional way.

Create a summary in this format:

# Short Summary
(3–4 sentences)

# Key Points
- bullet points
- short and objective

# Important Insights
- deeper observations

Here is the transcript:
{text}
    """

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(prompt)

    return response.text