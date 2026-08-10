from typing import List, TypedDict

class MarketResearchState(TypedDict):
    tech_data: str
    geo_data: str
    market_data: str
    final_trend_report: str
    critic_feedback: str
    critic_verdict: str
    revision_count: int
    past_reports: List[str]      # full archive (last 3)
    memory_digest: List[str]     # 🧠 compressed "banned concepts" lists (last 3)