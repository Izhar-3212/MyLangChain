from langgraph.graph import StateGraph, END
from state import MarketResearchState
from agents.researchers import tech_scout, geo_analyst, market_watcher
from agents.synthesizer import trend_synthesizer

def build_graph():
    workflow = StateGraph(MarketResearchState)

    # Add the nodes
    workflow.add_node("tech_scout", tech_scout)
    workflow.add_node("geo_analyst", geo_analyst)
    workflow.add_node("market_watcher", market_watcher)
    workflow.add_node("trend_synthesizer", trend_synthesizer)

    # Wire the edges (the flow)
    workflow.set_entry_point("tech_scout")
    workflow.add_edge("tech_scout", "geo_analyst")
    workflow.add_edge("geo_analyst", "market_watcher")
    workflow.add_edge("market_watcher", "trend_synthesizer")
    workflow.add_edge("trend_synthesizer", END)

    return workflow.compile()