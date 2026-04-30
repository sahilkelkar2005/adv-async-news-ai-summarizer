import os
from langchain_openai import ChatOpenAI

# 🔥 TEMP: paste your API key directly here
OPENROUTER_API_KEY = "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"

if not OPENROUTER_API_KEY:
    raise ValueError("API key missing")

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
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
    Summarize the following news clearly:

    {text}
    """

    response = llm.invoke(prompt)
    return response.content