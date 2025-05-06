import random

from playwright.sync_api import Page
from playwright.sync_api import Locator

class CardManager:

    def __init__(self, page: Page):
        self._page = page
        self.title_heading = page.get_by_role("heading", name="Creador de cartas Pokemon")
        self.name_input = page.get_by_role("textbox", name="Nombre *")
        self.life_input = page.get_by_role("spinbutton", name="Vida 1-100 *")
        self.speed_input = page.get_by_role("spinbutton", name="Velocidad 1-100 *")
        self.atack_input = page.get_by_role("spinbutton", name="Ataque 1-100 *")
        self.defense_input = page.get_by_role("spinbutton", name="Defensa 1-100 *")
        self.create_card = page.get_by_role("button", name="Crear Pokemon")

    
    def select_pokemon(self):
        """
            Encuentra las imagenes de pokemon que se encuentran disponible y selecciona una al azar
        """
        pokemons = [
            pokemon.get_attribute("alt") 
            for pokemon in self._page.get_by_test_id("list-of-pokemon-img").get_by_role("img").all()
            ]
        self._page.get_by_role("img", name=pokemons[random.randint(0, len(pokemons) - 1)]).click()
    
    def card_created(self, name: str) -> Locator:
        return self._page.get_by_alt_text(name)

    def card_created_delete(self, name: str):
        self._page.locator(f"//div[contains(@class, \"card\")]/div[@class=\"name\"]/h3[text()=\"{name}\"]/parent::div/parent::div/div/button").click()
