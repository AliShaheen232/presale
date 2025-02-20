from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Account(BaseModel):
    address: str
    chain: str


@app.get("/")
async def root() :
    return {"messgae":"presale APIs"}
