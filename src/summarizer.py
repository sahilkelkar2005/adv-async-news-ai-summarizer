import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env for local
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 🔐 Get API key (Streamlit → fallback to .env)
OPENROUTER_API_KEY = None

try:
    import streamlit as st
    if hasattr(st, "secrets") and "OPENROUTER_API_KEY" in st.secrets:
        OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
except:
    pass

if not OPENROUTER_API_KEY:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("API key not found. Add it in Streamlit secrets or .env")

# ✅ Initialize LLM (safe config)
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3,
    max_retries=2,          # 🔥 prevents hanging
    timeout=30              # 🔥 prevents infinite wait
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

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error during summarization: {str(e)}"