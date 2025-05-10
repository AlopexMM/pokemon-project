from uuid import uuid4
from .models import Pokemon
from uuid import UUID

import pathlib
import json
import asyncio

DATABASE = "database.json"

class Database:

    """
    Maneja la carga de la base de datos y el guardado de los datos en el archivo json
    """
    def __init__(self):
        self._memory_database = []
        if pathlib.Path(DATABASE).exists():
            json_text = pathlib.Path(DATABASE).read_text()
            json_object = json.loads(json_text)
            self._memory_database = [Pokemon.model_validate_json(json.dumps(obj)) for obj in json_object]
    
    def add(self, pokemon: Pokemon) -> list:
        self._memory_database.append(pokemon)
        self._save_file()
        return self._memory_database
    
    def remove(self, id: str) -> bool:
        self._memory_database = [pokemon for pokemon in self._memory_database if pokemon.id != id]
        self._save_file()
        return True

    def update(self, pokemon: Pokemon):
        copy = [poke for poke in self._memory_database if poke.id != pokemon.id]
        copy.append(pokemon)
        self._memory_database = copy
        self._save_file()
        return self._memory_database

    def _save_file(self):
        with open(DATABASE, "w") as file:
            json.dumps(
                [pokemon.model_dump() for pokemon in self._memory_database], 
                file
            )
    
    def pokemons(self):
        return self._memory_database
    
class PokemonRepo:

    def __init__(self):
        self._database = Database()
    
    def add(self, pokemon: Pokemon) -> list:
        pokemon.id = uuid4()
        return self._database.add(pokemon)
    
    def remove(self, id: UUID) -> bool:
        return self._database.remove(id)
    
    def update(self, pokemon: Pokemon) -> list:
        return self._database.update(pokemon)
    
    def pokemons(self) -> list:
        return self._database.pokemons()
    

    
