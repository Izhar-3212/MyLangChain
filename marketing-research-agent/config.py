import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama

load_dotenv()


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "qwen2.5:3b"),
            temperature=0.7,
            num_ctx=8192,   # room for research + old reports
        )
    elif provider == "openai":
        return ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o"), temperature=0.7)
    elif provider == "anthropic":
        return ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"), temperature=0.7)
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {provider}")


llm = get_llm()