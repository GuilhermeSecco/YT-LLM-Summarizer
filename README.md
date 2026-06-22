# 🎥 YT-LLM-Summarizer

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Gemini](https://img.shields.io/badge/LLM-Gemini%203.1%20Flash%20Lite-orange)
![Whisper](https://img.shields.io/badge/ASR-Whisper-green)
![YouTube](https://img.shields.io/badge/YouTube-Audio%20Extraction-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A Python tool that downloads YouTube videos, transcribes them, and generates high-quality summaries using LLMs (Gemini).

<p align='center'>
    <img width="500" alt="Thumbnail" src="https://github.com/user-attachments/assets/33dc7c59-1d6b-4cea-b468-33b4b4e078e3" />
</p>

## 📌 Overview
YT-LLM-Summarizer is a command-line tool that:

    Downloads YouTube video audio

    Converts it to WAV

    Transcribes using Whisper

    Summarizes using Google's Gemini 3.1 Flash Lite

    Produces English + Brazilian Portuguese output

    Saves a .md file using the video title as the filename

Fully automated.

Works on long videos (1h+).

Pipeline:
        
YouTube URL → Download (pytubefix) → Convert to WAV (ffmpeg) → Transcribe (Whisper) → Summarize (Gemini) → Markdown Output

## ❗ Gemini Limitations

The free tier has a limited RPM (requests per minute). If you hit a 429 error, wait a minute and try again, or enable billing in Google AI Studio.

## ⭐ Features

✔ Extract audio from any YouTube video

✔ Automatic transcription (Whisper)

✔ LLM summarization with structured output

✔ Summary in English + PT-BR

✔ Cleans temporary files automatically

✔ Video title used as output filename

✔ CLI and “Run” mode support (input prompt)

## 📂 Project Structure

    YT-LLM-Summarizer/
    ├── src/
    │   ├── downloader.py
    │   ├── converter.py
    │   ├── summarizer.py
    ├── summaries/
    ├── temp/ (auto-created and auto-deleted)
    ├── main.py
    ├── .env
    ├── README.md
    ├── uv.lock
    └── pyproject.toml

## 📦 Dependencies

    pytubefix
        
    ffmpeg (system)
        
    openai-whisper
        
    google-generativeai
        
    python-dotenv

## 🛠 Installation

1. Install ffmpeg    

   On Windows, open your powershell and use:
   
        winget install ffmpeg

2. Create a Gemini API Key

    Learn how to do it here:
   
        https://ai.google.dev/gemini-api/docs/api-key
            
3. Clone the repo
   
        git clone https://github.com/GuilhermeSecco/YT-LLM-Summarizer
        cd YT-LLM-Summarizer

5. Install dependencies

         uv sync

6. Create your .env
   
        GOOGLE_API_KEY=your_key_here

## ▶️ Usage

Mode 1 — Terminal

    uv run main.py --url "https://youtube.com/watch?v=..."

Mode 2 — PyCharm or VSCode Button (Run)

    Run → program asks:
    └── Enter YouTube URL:

## 📄 Output Example

    summaries/
     └── Lore of Risk of Rain - The Tragic Story of Two Brothers.md

Content includes:

    Summary (EN)

    Key Insights (EN)
    
    Notes (EN)
    
    Resumo (PT-BR)
    
    Pontos Chave (PT-BR)
    
    Extra (PT-BR)
