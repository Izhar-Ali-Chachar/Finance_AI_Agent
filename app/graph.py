# app/graph.py

from langgraph.graph import StateGraph, START, END 
from app.types import FinanceState
from app.nodes import news_agent, stock_agent, summary_agent

graph = StateGraph(FinanceState)

graph.add_node("news_agent", news_agent)
graph.add_node("stock_agent", stock_agent)
graph.add_node("summary_agent", summary_agent)

graph.add_edge(START, "news_agent")
graph.add_edge("news_agent", "stock_agent")
graph.add_edge("stock_agent", "summary_agent")
graph.add_edge("summary_agent", END)

finance_app = graph.compile()
