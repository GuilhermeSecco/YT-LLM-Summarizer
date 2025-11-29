🎥 YT-LLM-Summarizer

> A Python tool that downloads YouTube videos, transcribes them, and generates high-quality summaries using LLMs (Gemini).

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
    ├── temp/ # auto-created and auto-deleted
    ├── main.py
    ├── .env
    ├── README.md
    ├── uv.lock
    └── pyproject.toml

## 🛠 Installation
Requires:

    Python 3.12+
    
    ffmpeg installed and added to PATH
    
    uv package manager (recommended)
    
    Google AI Studio API Key
    
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
        ├── temp/ # auto-created and auto-deleted
        ├── main.py
        ├── .env
        ├── README.md
        ├── uv.lock
        └── pyproject.toml

## 🛠 Instalação

Requisitos:
    
    Python 3.12+
    
    ffmpeg instalado e adicionado ao PATH
    
    uv package manager (recomendado)
    
    Chave própria do Google AI Studio API

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


