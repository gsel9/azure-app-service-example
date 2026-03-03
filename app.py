from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Query(BaseModel):
    """
    Data model for user message.
    """
    message: str


# TODO: Depends - User authentication
@app.post("/ask")
async def ask_api(query: Query) -> Dict[str, Any]:
    """
    Endpoint to execute chat loop.
    """
    return {"The recieved message": query.message}
    