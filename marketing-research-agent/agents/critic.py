from config import llm

MAX_REVISIONS = 2


def trend_critic(state):
    print("🧐 Critic is reviewing the draft...")

    memory_note = ""
    digests = state.get("memory_digest") or []
    if digests:
        digest_lines = "\n".join(digests)
        memory_note = f"""
PAST SESSIONS COVERED (use for the NOVELTY check):
{digest_lines}
"""

    prompt = f"""
You are a ruthless editorial critic for a top-tier market intelligence firm.
You hate generic AI buzzwords, vague claims, and ideas not grounded in data.

{memory_note}

Here is a draft trend report written by your junior analyst:

{state['final_trend_report']}

Judge it against these criteria:
1. SPECIFICITY: Does each trend cite concrete signals (real companies, regions, technologies, events)?
2. INTERSECTION: Does each trend genuinely connect tech + geopolitics + markets, not just mention them separately?
3. BOLDNESS: Are the product ideas non-obvious, or just "ChatGPT for X"?
4. NOVELTY: Does any trend or product repeat something from PAST SESSIONS — even renamed, like "X 2.0" or "X Pro"? If yes → REVISE.

Respond in EXACTLY this format:
VERDICT: APPROVE or REVISE
FEEDBACK: <if REVISE, list the specific weaknesses to fix. If APPROVE, write "None">
"""

    response = llm.invoke(prompt)
    text = response.content
    upper = text.upper()

    verdict = "REVISE" if "REVISE" in upper else "APPROVE"

    feedback = ""
    idx = upper.find("FEEDBACK:")
    if idx != -1:
        feedback = text[idx + len("FEEDBACK:"):].strip()

    count = state.get("revision_count", 0)

    if verdict == "REVISE" and count < MAX_REVISIONS:
        count += 1
        print(f"🔁 Critic demands a rewrite ({count}/{MAX_REVISIONS})")
        return {
            "critic_verdict": "REVISE",
            "critic_feedback": feedback,
            "revision_count": count,
        }

    if verdict == "REVISE":
        print("⏹️ Max revisions reached — shipping current draft.")
    else:
        print("✅ Critic approved the report!")

    return {"critic_verdict": "APPROVE", "critic_feedback": feedback}
