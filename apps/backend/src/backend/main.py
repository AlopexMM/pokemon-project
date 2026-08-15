from fastapi import FastAPI
from repositories.config import create_db
from api.pokemon import pokemon_router

import uvicorn

app = FastAPI()

app.include_router(pokemon_router, prefix="/api")

if __name__ == "__main__":
    create_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)