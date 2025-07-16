from langgraph.graph import StateGraph, START, END
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import yfinance as yf


wrapper = DuckDuckGoSearchAPIWrapper(max_results=2)

search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")

ticker = yf.Ticker("MSFT")

print(ticker.info["currentPrice"])

