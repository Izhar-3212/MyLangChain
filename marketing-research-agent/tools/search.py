from langchain_community.tools import DuckDuckGoSearchRun

# One shared search tool used by all researcher agents
search_tool = DuckDuckGoSearchRun()