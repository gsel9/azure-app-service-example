from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/ask")
async def ask_api(request: Request):
    response = {
        "headers": request.headers,
        "query_params ": request.query_params
    }
    return {"response": "Hello to you!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
