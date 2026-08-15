from sqlmodel import create_engine, SQLModel, Session
from schemas.pokemon import PokemonSchema

import json

engine = create_engine("sqlite:///pokemon.db", echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        pokemons = json.load(open("pokemon_data.json"))
        for pokemon in pokemons:
            pokemon = PokemonSchema(
                uid=pokemon["uid"],
                name=pokemon["name"],
                elements=pokemon["elements"],
                hp=pokemon["hp"],
                attack=pokemon["attack"],
                defense=pokemon["defense"],
                special_attack=pokemon["sp_attack"],
                special_defense=pokemon["sp_def"],
                speed=pokemon["speed"],
                icon=f"{pokemon['name'].lower()}.png",
                icon_alt=pokemon['name'].lower(),
                img=f"{pokemon['name'].lower()}.jpg")
            session.add(pokemon)
        session.commit()
