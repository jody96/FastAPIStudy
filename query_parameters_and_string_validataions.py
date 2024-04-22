from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

@app.get("/items/")
async def read_items(hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None):
    if hidden_query:
        return {"hidden_query" : hidden_query}
    else:
        return {"hidden_query": "Not found"}