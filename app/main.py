# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import finance_app

app = FastAPI()

class FinanceRequest(BaseModel):
    query: str
    ticker: str

@app.post("/analyze")
def analyze_finance(data: FinanceRequest):
    result = finance_app.invoke(data.dict())
    return {"summary": result["summary"]}
