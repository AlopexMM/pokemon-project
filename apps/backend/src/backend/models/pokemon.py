from pydantic import BaseModel

class PokemonResponse(BaseModel):
    uid: str
    name: str
    elements: list[str]
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    icon: str
    icon_alt: str
    img: str