# app/types.py

from typing import TypedDict

class FinanceState(TypedDict):
    query: str
    ticker: str
    news: str
    market: str
    summary: str
