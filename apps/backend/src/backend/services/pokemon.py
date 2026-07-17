from repositories.pokemon import PokemonRepository
from models.pokemon import PokemonResponse

def get_all_pokemon_db() -> list[PokemonResponse]:
    repository = PokemonRepository()
    pokemons = repository.get_all()
    return [PokemonResponse(
        pokemon_id=pokemon.pokemon_id,
        name=pokemon.name,
        elements=pokemon.elements.split(","),
        hp=pokemon.hp,
        attack=pokemon.attack,
        defense=pokemon.defense,
        special_attack=pokemon.special_attack,
        special_defense=pokemon.special_defense,
        speed=pokemon.speed,
        icon=pokemon.icon,
        img=pokemon.img
    ) for pokemon in pokemons]