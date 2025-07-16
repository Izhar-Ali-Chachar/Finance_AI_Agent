# app/nodes.py

from app.types import FinanceState
from app.config import llm
from langchain_community.tools import DuckDuckGoSearchRun
import yfinance as yf

search = DuckDuckGoSearchRun()

def news_agent(state: FinanceState) -> FinanceState:
    news = search.run(f"{state['query']} financial news")
    return {**state, "news": news}

def stock_agent(state: FinanceState) -> FinanceState:
    stock = yf.Ticker(state["ticker"])
    info = stock.info
    hist = stock.history(period="5d")
    summary = f"{info.get('longBusinessSummary', 'N/A')}\n\nHistory:\n{hist.tail()}"
    return {**state, "market": summary}

def summary_agent(state: FinanceState) -> FinanceState:
    prompt = f"""
You are a financial analyst. Analyze this:

News:
{state['news']}

Stock Data:
{state['market']}

Provide a concise investment summary.
"""
    response = llm.invoke(prompt)
    return {**state, "summary": response.content}
