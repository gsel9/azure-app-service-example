from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Query(BaseModel):
    message: str


@app.post("/ask")
async def ask_api(query: Query) -> Dict[str, Any]:
    return {"Input": query.message}
