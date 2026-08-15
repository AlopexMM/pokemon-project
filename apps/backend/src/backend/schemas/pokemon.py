from sqlmodel import SQLModel, Field

class PokemonSchema(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    uid: str
    name: str
    elements: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    icon: str
    icon_alt: str
    img: str