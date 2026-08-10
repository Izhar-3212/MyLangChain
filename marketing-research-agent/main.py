from graph import build_graph
from report import render_report   # ← new

def main():
    print("🚀 Starting Marketing Intelligence Run...\n")

    app = build_graph()

    # Pass an empty state; the graph fills it in as it flows through nodes
    final_state = app.invoke({})

    print("\n" + "="*60)
    print("🔮 FINAL FUTURE TRENDS REPORT")
    print("="*60 + "\n")
    print(final_state["final_trend_report"])

    render_report(final_state["final_trend_report"])   # ← new

if __name__ == "__main__":
    main()