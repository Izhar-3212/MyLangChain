# 🔮 Multi-Agent Marketing Research System

An experimental **LangChain + LangGraph** project where a team of AI research
agents scans the live web (tech, geopolitics, markets) and synthesizes the
signals into future-facing trend reports — rendered as a styled HTML dashboard.

## 🤖 The Agent Team

| Node | Role |
|------|------|
| 🔍 `tech_scout` | Searches trending tech, AI tools & consumer products |
| 🌍 `geo_analyst` | Searches geopolitical shifts & global news |
| 📈 `market_watcher` | Searches trading updates & emerging services |
| 🧠 `trend_synthesizer` | Connects the dots → writes future trends & product ideas |

**Flow:** `START → tech_scout → geo_analyst → market_watcher → trend_synthesizer → HTML report → END`

## 🛠️ Stack

- **LangGraph** – stateful agent orchestration
- **LangChain** – LLM & tool integrations
- **Ollama + Qwen2.5-3B** – free local LLM (no API key)
- **DuckDuckGo Search** – live web search (no API key)
- **markdown** – HTML report rendering

## 🚀 Setup

1. Install [Ollama](https://ollama.com), then pull the model:
   ```bash
   ollama pull qwen2.5:3b
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Check `.env` (`LLM_PROVIDER=ollama`), then run:
   ```bash
   python main.py
   ```

The report auto-opens in your browser and is saved under `reports/`.

## 📁 Project Structure

```
marketing-research-agent/
├── main.py          # entry point
├── config.py        # LLM provider switch (ollama / openai / anthropic)
├── state.py         # shared graph state
├── graph.py         # LangGraph workflow
├── report.py        # HTML report renderer
├── tools/search.py  # DuckDuckGo search tool
└── agents/          # researcher + synthesizer nodes
```

## 🧪 Experiment Log

- ✅ v1 — sequential multi-agent research + synthesis (local LLM)
- ✅ v2 — styled HTML trend report
- 🔜 v3 — parallel researchers / self-correcting critic loop