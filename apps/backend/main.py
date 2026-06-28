from fastapi import FastAPI
from sqlmodel import SQLModel

from .db import engine

SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
async def root():
    pass

@app.get("/:id")
async def get_pokemon(id: str):
    pass

@app.post("/")
async def create_pokemon(pokemon: PokemonStats):
    pass

@app.put("/:id")
async def update_pokemon(id: str, pokemon: PokemonStats):
    pass

@app.delete("/:id")
async def delete_pokemon(id: str):
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)