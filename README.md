# 🎥 YT-LLM-Summarizer

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.0%20Flash-orange)
![Whisper](https://img.shields.io/badge/ASR-Whisper-green)
![YouTube](https://img.shields.io/badge/YouTube-Audio%20Extraction-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A Python tool that downloads YouTube videos, transcribes them, and generates high-quality summaries using LLMs (Gemini).

<p align='center'>
    <img width="500" alt="Thumbnail" src="https://github.com/user-attachments/assets/33dc7c59-1d6b-4cea-b468-33b4b4e078e3" />
</p>

# 🇺🇸 English
## 📌 Overview
YT-LLM-Summarizer is a command-line tool that:

    Downloads YouTube video audio

    Converts it to WAV

    Transcribes using Whisper

    Summarizes using Google's Gemini 2.0 Flash

    Produces English + Brazilian Portuguese output

    Saves a .md file using the video title as the filename

Fully automated.

Works on long videos (1h+).

Pipeline:
        
YouTube URL → Download (pytubefix) → Convert to WAV (ffmpeg) → Transcribe (Whisper) → Summarize (Gemini) → Markdown Output

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
    
1. Clone the repo
   
        git clone https://github.com/<your-user>/YT-LLM-Summarizer
   
        cd YT-LLM-Summarizer

2. Install dependencies

         uv install

3. Create your .env
   
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

## 🧠 Why this project matters

This tool demonstrates:

    Multimodal processing (audio + text)
        
    Integration of ASR + LLMs
        
    Automation pipelines
        
    Clean code organization
        
    Practical GenAI applied to real data

# 🇧🇷 Português
## 📌 Visão Geral

YT-LLM-Summarizer é uma ferramenta em Python que:

    Baixa o áudio de vídeos do YouTube
    
    Converte para WAV
    
    Transcreve usando Whisper
    
    Resume usando Gemini 2.0 Flash
    
    Gera resumos em EN + PT-BR
    
    Salva o arquivo .md com o título real do vídeo

Totalmente automatizado.

Funciona com vídeos longos (1h+).

## ⭐ Funcionalidades

✔ Baixa áudio de vídeos do YouTube

✔ Transcrição automática

✔ Resumo estruturado com LLM

✔ Texto final em inglês e português

✔ Limpeza automática da pasta temp

✔ Nome do arquivo baseado no título

✔ Suporte a terminal e execução direta

## 📂 Estrutura do Projeto

    YT-LLM-Summarizer/
        ├── src/
        │   ├── downloader.py
        │   ├── converter.py
        │   ├── summarizer.py
        ├── summaries/
        ├── temp/ (Criado automaticamente durante o uso e excluído após o término do programa)
        ├── main.py
        ├── .env
        ├── README.md
        ├── uv.lock
        └── pyproject.toml

## 📦 Dependencias

    pytubefix
        
    ffmpeg (system)
        
    openai-whisper
        
    google-generativeai
        
    python-dotenv

## 🛠 Instalação

1. Clone o repositório
   
        git clone https://github.com/<your-user>/YT-LLM-Summarizer
   
        cd YT-LLM-Summarizer

2. Instale as Dependências

         uv install

3. Crie o seu .env
   
        GOOGLE_API_KEY=your_key_here

## ▶️ Uso

Primeira Forma — Terminal

    uv run main.py --url "https://youtube.com/watch?v=..."

Segunda Forma — Utilizando o botão run no Pycharm ou VSCode

    Run → O programa pede:
    └── Enter YouTube URL:

## 📄 Exemplo do arquivo resultante

    summaries/
     └── Projetos REALMENTE úteis para iniciantes em Python.md

Resultado Inclui:

    Summary (EN)

    Key Insights (EN)
    
    Notes (EN)
    
    Resumo (PT-BR)
    
    Pontos Chave (PT-BR)
    
    Extra (PT-BR)


