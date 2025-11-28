from pathlib import Path
import whisper
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Loading API Key
load_dotenv()

# Configuring Gemini
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
    You are generating a clean, concise and natural summary of a YouTube video.
    Below is the raw transcript.

    Your goals:
    - Produce a short, human-sounding summary (not robotic or repetitive).
    - Focus on the main ideas mentioned ONLY in the transcript.
    - Avoid adding invented details or misinterpreting library names.
    - Keep the summary fluid, natural, and clear.
    - After writing the English version, provide a Brazilian Portuguese version with the same structure.
    - Preserve the original tone of the speaker when appropriate.
    - In PT-BR, translate meaningfully, not word-for-word.
    - Remove filler words or repeated ideas from the transcript.

    Transcript:
    {text}

    Now return the following sections, first in English, then in Brazilian Portuguese:
    
    --- English ---
    
    ### Summary
    A natural, well-written paragraph describing the main ideas discussed in the video.

    ### Key Insights
    3–5 short bullet points capturing the most important takeaways.

    ### Notes
    Small clarifications that were mentioned in the transcript, without speculation.

    --- Português ---

    ### Resumo
    Tradução natural do resumo acima, com tom humano e claro.

    ### Pontos Chave
    Tradução dos insights acima, mantendo significado e objetividade.

    ### Extra
    Tradução fiel das notas acima, sem adicionar conteúdo.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(prompt)

    return response.text