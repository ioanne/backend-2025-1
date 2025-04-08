from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Usuario(BaseModel):
    id: int
    nombre: str


@app.get("/")
async def home():
    return {"message": "Página de home 2!"}

