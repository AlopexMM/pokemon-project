from fastapi import APIRouter
from models.pokemon import PokemonResponse
from services.pokemon import get_all_pokemon_db

pokemon_router = APIRouter()

@pokemon_router.get(
    "/all",
    response_model=list[PokemonResponse],
    )
def get_all_pokemon():
    return get_all_pokemon_db()