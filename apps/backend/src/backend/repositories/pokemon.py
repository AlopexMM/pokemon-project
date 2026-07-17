from schemas.pokemon import PokemonSchema
from sqlmodel import Session, select
from .config import engine

class PokemonRepository:

    def __init__(self):
        self.session = Session(engine)
    
    def get_all(self):
        with self.session as session:
            return session.exec(select(PokemonSchema)).all()