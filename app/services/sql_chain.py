import os
import re
import json
import traceback
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities.sql_database import SQLDatabase


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

sql_prompt = PromptTemplate(
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
- If format is "table", return a JSON object like:
  {{"type": "table", "data": [{{"column1": "value", "column2": "value"}}]}}
- If format is "graph", return a JSON object like:
  {{"type": "graph", "x": "label_field", "y": "value_field", "data": [{{"label": "X", "value": 100}}]}}

Only return the JSON object — no markdown or explanation.
"""
)

sql_llm_chain = LLMChain(llm=llm, prompt=sql_prompt)


db = SQLDatabase.from_uri(os.getenv("MYSQL_URI"))


sql_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)


def extract_format(question: str) -> str:
    q = question.lower()
    if "table" in q:
        return "table"
    elif "graph" in q or "chart" in q:
        return "graph"
    return "text"


def extract_sql_from_response(response: str) -> str:
    cleaned = re.sub(r"```sql|```", "", response, flags=re.IGNORECASE).strip()
    
  
    match = re.search(r"SELECT\s.+?;", cleaned, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(0).strip()

    raise ValueError("Could not extract a valid SQL query from LLM response.")



def run_sql_chain(question: str) -> dict:
    try:
        format_requested = extract_format(question)

     
        sql_generation_response = sql_chain.run(question)
        pure_sql = extract_sql_from_response(sql_generation_response)

       
        result_rows = db._execute(pure_sql)

        structured_data = result_rows

        if not structured_data:
 
            if format_requested == "table":
                return {
                "format": "table",
                "data": {
                    "type": "table",
                    "data": []
                }
                }
        elif format_requested == "graph":
            return {
                "format": "graph",
                "data": {
                    "type": "graph",
                    "x": "",
                    "y": "",
                    "data": []
                }
            }
        else:
            return {
                "format": "text",
                "data": {
                    "type": "text",
                    "message": "No data found for your query."
                }
            }


        final_response = sql_llm_chain.run({
            "data": structured_data,
            "question": question,
            "format": format_requested
        })

        try:
            parsed = json.loads(final_response)
        except json.JSONDecodeError:
            parsed = final_response 
        return {
            "format": format_requested,
            "data": parsed
        }

    except Exception as e:
        print("🔥 Full traceback:\n", traceback.format_exc())
        return {
            "format": "error",
            "data": f" SQL Chain Error: {str(e)}"
        }
