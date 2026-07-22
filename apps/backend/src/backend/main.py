from fastapi import FastAPI
from repositories.config import create_db
from api.pokemon import pokemon_router
from ui.pokemon_page import ui_router

import uvicorn

app = FastAPI()

app.include_router(pokemon_router, prefix="/api")
app.include_router(ui_router)

if __name__ == "__main__":
    create_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)