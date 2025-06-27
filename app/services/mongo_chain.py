import os
import json
import traceback
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate


load_dotenv()


client = MongoClient( "mongodb://localhost:27017/")
db = client["wealth_portfolio"]
users_collection = db["users"]


llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)


mongo_prompt = PromptTemplate(
    input_variables=["data", "question", "format"],
    template="""
You are a helpful assistant.

Given the user data below:
{data}

The user has asked this question:
{question}

They want the answer in format: {format}

👉 Respond according to format:
- If format is "text", return a plain natural language response.
- If format is "table", return a raw JSON object like:
  {{"type": "table", "data": [{{"column1": "value", "column2": "value"}}]}}
- If format is "graph", return a raw JSON object like:
  {{"type": "graph", "x": "label_field", "y": "value_field", "data": [{{"label": "X", "value": 100}}]}}

⚠️ Only return the JSON object. No markdown, no ``` or extra formatting.
"""
)


mongo_chain = LLMChain(llm=llm, prompt=mongo_prompt)


def extract_format(question: str) -> str:
    q = question.lower()
    if "table" in q:
        return "table"
    elif "graph" in q or "chart" in q:
        return "graph"
    return "text"


def run_mongo_chain(question: str) -> dict:
    try:
        format_requested = extract_format(question)
        users = list(users_collection.find({}, {"_id": 0}))

        response = mongo_chain.run({
            "data": users,
            "question": question,
            "format": format_requested
        })

        
        if format_requested in ["table", "graph"]:
            try:
                response = json.loads(response)
            except json.JSONDecodeError:
                return {
                    "format": "error",
                    "data": {
                        "error": " Failed to parse LLM response as JSON.",
                        "raw": response
                    }
                }

        return {
            "format": format_requested,
            "data": response
        }

    except Exception as e:
        print("🔥 Error in Mongo Chain:", traceback.format_exc())
        return {
            "format": "error",
            "data": f" Mongo Chain Error: {str(e)}"
        }
