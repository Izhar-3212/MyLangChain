from config import llm


def trend_synthesizer(state):
    revision = state.get("revision_count", 0)
    if revision > 0:
        print(f"🧠 Synthesizer is rewriting (revision {revision})...")
    else:
        print("🧠 Synthesizer is connecting the dots...")

    memory_block = ""
    digests = state.get("memory_digest") or []
    if digests:
        banned = "\n".join(f"- {d}" for d in digests)
        memory_block = f"""
YOUR LONG-TERM MEMORY — ALREADY COVERED IN PAST SESSIONS (BANNED):
{banned}

HARD RULE: You must NOT reuse these trend names, product names, or their core
concepts. Find DIFFERENT signals in today's research data.
Repeating a banned concept = automatic failure.
"""

    feedback_block = ""
    if state.get("critic_feedback"):
        feedback_block = f"""
YOUR PREVIOUS DRAFT WAS REJECTED. THE CRITIC SAID:
{state['critic_feedback']}

Rewrite the report, directly addressing every point above.
"""

    prompt = f"""
You are a visionary Marketing Strategist and Futurist.
Your job is to look at disparate data points and find the "white space" for future business ideas.

Here is the raw intelligence gathered by your research team today:

[TECH & PRODUCTS]:
{state['tech_data']}

[GEOPOLITICS & NEWS]:
{state['geo_data']}

[MARKETS & TRADING]:
{state['market_data']}

{memory_block}

{feedback_block}

Task: Synthesize this into 3 highly specific, future-facing market trends and product ideas.
For each idea, provide:
1. The Name of the Trend
2. The "Why" (how the tech, geopolitics, and markets intersect to create this)
3. A Concrete Future Product or Marketing Angle to capitalize on it.

Rules:
- No generic buzzwords. Every idea must cite a specific signal from the research data.
- Ideas must be bold and non-obvious.
- Never reuse a banned concept from memory, even renamed.
"""

    response = llm.invoke(prompt)
    return {"final_trend_report": response.content}