from config import llm

def trend_synthesizer(state):
    print("🧠 Synthesizer is connecting the dots...")

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

Task: Synthesize this into 3 highly specific, future-facing market trends and product ideas.
For each idea, provide:
1. The Name of the Trend
2. The "Why" (how the tech, geopolitics, and markets intersect to create this)
3. A Concrete Future Product or Marketing Angle to capitalize on it.
"""

    response = llm.invoke(prompt)
    return {"final_trend_report": response.content}