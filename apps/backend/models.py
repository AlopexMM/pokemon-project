from enum import Enum
from pydantic import BaseModel, Field
from typing import Annotated
from uuid import UUID, uuid4

class PokemonElement(Enum):
    normal = "NORMAL"
    fire = "FIRE"
    water = "WATER"
    electric = "ELECTRIC"
    grass = "GRASS"
    ice = "ICE"
    fighting = "FIGHTING"
    poison = "POISON"
    ground = "GROUND"
    flying = "FLYING"
    psychic = "PSYCHIC"
    bug = "BUG"
    rock = "ROCK"
    ghost = "GHOST"
    dragon = "DRAGON"
    dark = "DARK"
    steel = "STEEL"
    fairy = "FAIRY"



class PokemonStats(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    pokemon_id: str
    name: str
    element: Annotated[list[PokemonElement], Field(default_factory=list)]
    hp: Annotated[int, Field(gt=0)]
    defense: Annotated[int, Field(gt=0)]
    sp_atk: Annotated[int, Field(gt=0)]
    sp_def: Annotated[int, Field(gt=0)]
    speed: Annotated[int, Field(gt=0)]

