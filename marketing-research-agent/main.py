from langgraph.checkpoint.sqlite import SqliteSaver
from graph import build_graph
from report import render_report

THREAD_ID = "marketing-research-main"


def main():
    print("🚀 Starting Marketing Intelligence Run...\n")

    with SqliteSaver.from_conn_string("checkpoints.db") as checkpointer:
        app = build_graph(checkpointer=checkpointer)
        config = {"configurable": {"thread_id": THREAD_ID}}

        # Peek at long-term memory before running
        snapshot = app.get_state(config)
        past = snapshot.values.get("past_reports") or []
        print(f"🧠 Long-term memory: {len(past)} past report(s) on file.\n")

        final_state = app.invoke({}, config)

    print("\n" + "="*60)
    print("🔮 FINAL FUTURE TRENDS REPORT")
    print("="*60 + "\n")
    print(final_state["final_trend_report"])

    render_report(final_state["final_trend_report"])


if __name__ == "__main__":
    main()