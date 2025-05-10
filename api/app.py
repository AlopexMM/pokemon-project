from typing import Union
from fastapi import FastAPI
from uuid import UUID

from .repository import PokemonRepo
from .models import Pokemon

import json

app = FastAPI()
database = PokemonRepo()

@app.get("/")
def index():
    return {"urls":["/pokemon","pokemon/id"] }

# Metodo GET para URL pokemon/
# Debe devolver un listado de los pokemon que se encuentran en la base de datos
@app.get("/pokemon")
def pokemon_list():
    return database.pokemons()

# Metodo POST para URL pokemon/
# Debe devolver un listado de pokemons junto con el que se agrego
@app.post("/pokemon")
def add_pokemon(pokemon: Pokemon):
    return database.add(pokemon)

# Metodo PUT para URL pokemon/
# Debe devolver un listado actualizado de pokemons
@app.put("/pokemon/{id}")
def update_pokemon(id: str, pokemon: Pokemon):
    return database.update(pokemon)

# Metodo DELETE para la URL pokemon/id
# Debe devolver un bool
@app.delete("/pokemon/{id}")
def delete_pokemon(id: UUID):
    return database.remove(id)