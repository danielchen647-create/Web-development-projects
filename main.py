from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow any origin (fine for local learning only)
    allow_methods=["*"],  # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # allow headers like Content-Type
)


class Item(BaseModel):
    name: str
    price: float
    people: list[str]


@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend!"}


@app.post("/api/split")
def split(items: list[Item]):
    totals = {}
    for item in items:
        if not item.people:
            continue
        share = item.price / len(item.people)
        for person in item.people:
            totals[person] = round(totals.get(person, 0) + share, 2)
    return totals
