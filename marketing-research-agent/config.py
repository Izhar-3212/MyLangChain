import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama

load_dotenv()

def get_llm():
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        return ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.2"), temperature=0.7)
    elif provider == "openai":
        return ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o"), temperature=0.7)
    elif provider == "anthropic":
        return ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"), temperature=0.7)
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {provider}")

# One shared brain used by all agents
llm = get_llm()