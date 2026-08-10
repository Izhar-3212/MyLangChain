from config import llm

def archivist(state):
    print("🗄️ Archivist is filing this report into long-term memory...")

    past = state.get("past_reports") or []
    past = (past + [state["final_trend_report"]])[-3:]

    # Compress the report into a short banned-concepts digest
    digest_prompt = f"""
List every trend name and product name mentioned in the report below.
Output ONLY a comma-separated list. No sentences, no numbering, no extra words.

REPORT:
{state['final_trend_report']}
"""
    digest = llm.invoke(digest_prompt).content.strip()
    print(f"🗄️ Memory digest saved: {digest[:100]}")

    digests = state.get("memory_digest") or []
    digests = (digests + [digest])[-3:]

    return {"past_reports": past, "memory_digest": digests}
