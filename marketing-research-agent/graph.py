from langgraph.graph import StateGraph, END
from state import MarketResearchState
from agents.researchers import tech_scout, geo_analyst, market_watcher
from agents.synthesizer import trend_synthesizer
from agents.critic import trend_critic
from agents.archivist import archivist


def route_critic(state):
    if state.get("critic_verdict") == "REVISE":
        return "rewrite"
    return "ship_it"


def build_graph(checkpointer=None):
    workflow = StateGraph(MarketResearchState)

    workflow.add_node("tech_scout", tech_scout)
    workflow.add_node("geo_analyst", geo_analyst)
    workflow.add_node("market_watcher", market_watcher)
    workflow.add_node("trend_synthesizer", trend_synthesizer)
    workflow.add_node("trend_critic", trend_critic)
    workflow.add_node("archivist", archivist)

    workflow.set_entry_point("tech_scout")
    workflow.add_edge("tech_scout", "geo_analyst")
    workflow.add_edge("geo_analyst", "market_watcher")
    workflow.add_edge("market_watcher", "trend_synthesizer")
    workflow.add_edge("trend_synthesizer", "trend_critic")

    workflow.add_conditional_edges(
        "trend_critic",
        route_critic,
        {
            "rewrite": "trend_synthesizer",
            "ship_it": "archivist",   # approved reports get filed into memory
        },
    )
    workflow.add_edge("archivist", END)

    return workflow.compile(checkpointer=checkpointer)