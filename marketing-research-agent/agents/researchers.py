from tools.search import search_tool

def tech_scout(state):
    print("🔍 Tech Scout is searching...")
    query = "latest technology advancements, trending AI tools, upcoming consumer tech products"
    result = search_tool.run(query)
    return {"tech_data": result}

def geo_analyst(state):
    print("🌍 Geo Analyst is searching...")
    query = "current geopolitical situations affecting global markets, supply chain shifts, major world news"
    result = search_tool.run(query)
    return {"geo_data": result}

def market_watcher(state):
    print("📈 Market Watcher is searching...")
    query = "trending trading updates, emerging consumer services, stock market technology shifts"
    result = search_tool.run(query)
    return {"market_data": result}