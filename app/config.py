import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Missing GOOGLE_API_KEY in environment")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)