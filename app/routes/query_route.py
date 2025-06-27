from fastapi import APIRouter
from pydantic import BaseModel
from app.services.router import decide_data_source
from app.services.sql_chain import run_sql_chain
from app.services.mongo_chain import run_mongo_chain

router = APIRouter()

class QueryInput(BaseModel):
    question: str

@router.post("/query")
async def handle_query(input_data: QueryInput):
    question = input_data.question
    source = decide_data_source(question)

    if source == "mysql":
        response = run_sql_chain(question)
    elif source == "mongodb":
        response = run_mongo_chain(question)
    elif source == "both":
        response = {
            "mysql": run_sql_chain(question),
            "mongodb": run_mongo_chain(question)
        }
        return {
            "question": question,
            "decided_data_source": source,
            "response": response
        }
    else:
        response = {"format": "text", "data": "? Could not determine appropriate data source."}

    return {
        "question": question,
        "decided_data_source": source,
        "format": response.get("format", "text"),
        "response": response.get("data", "")
    }

@router.get("/")
def read_root():
    return {"message": " FastAPI server is running!"}
