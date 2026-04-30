import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env for local
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 🔥 Safe way to access Streamlit secrets (no crash)
OPENROUTER_API_KEY = None

try:
    import streamlit as st
    if "OPENROUTER_API_KEY" in st.secrets:
        OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
except Exception:
    pass  # ignore if not running on Streamlit Cloud

# Fallback to .env (local)
if not OPENROUTER_API_KEY:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("API key not found. Add it in .env or Streamlit secrets.")

# LLM setup
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3
)

def summarize(docs):
    try:
        text = "\n".join([d.page_content for d in docs])
    except:
        text = "\n".join(docs)

    prompt = f"""
Summarize the following news in a clear and concise way:

{text}
"""

    response = llm.invoke(prompt)
    return response.content