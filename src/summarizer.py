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
    Você é um assistente especializado em resumir aulas acadêmicas e técnicas.
    Abaixo está a transcrição de uma aula.

    Seu objetivo é produzir um resumo completo e didático que permita ao aluno
    compreender toda a matéria sem precisar assistir à aula.

    Regras:
    - Não omita conceitos, definições ou exemplos importantes.
    - Mantenha a ordem lógica em que os tópicos foram apresentados.
    - Use linguagem clara e direta, sem ser robótico.
    - Se houver fórmulas, passos ou processos, descreva-os com precisão.
    - Não invente conteúdo que não esteja na transcrição.
    - Ignore repetições, pausas e falas irrelevantes do professor.

    Transcrição:
    {text}

    Retorne as seguintes seções:

    ### Resumo Geral
    Um parágrafo introdutório descrevendo o tema central da aula e o que foi abordado.

    ### Conteúdo da Aula
    Os tópicos explicados na aula, em ordem, com explicações completas.
    Use subtítulos (####) para separar cada tópico quando necessário.

    ### Definições e Conceitos-Chave
    Lista dos termos, definições e conceitos importantes mencionados na aula.

    ### Exemplos e Aplicações
    Exemplos práticos, exercícios ou aplicações que o professor apresentou.
    Se não houver, omita esta seção.

    ### Pontos de Atenção
    Alertas, dicas ou observações que o professor enfatizou durante a aula.
    """

    model = genai.GenerativeModel("gemini-3.1-flash-lite")

    response = model.generate_content(prompt)

    return response.text