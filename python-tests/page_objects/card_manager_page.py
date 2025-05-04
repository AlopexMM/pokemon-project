from playwright.sync_api import Page
from playwright.sync_api import Locator

class CardManager:

    def __init__(self, page: Page):
        self.page = page
        self.title_heading = page.get_by_role("heading", name="Creador de cartas Pokemon")
    
    def select_pokemon(self):
        """
            Encuentra las imagenes de pokemon que se encuentran disponible y selecciona una al azar
        """
        pokemons = [
            pokemon.get_attribute("alt") 
            for pokemon in self.page.get_by_test_id("list-of-pokemon-img").get_by_role("img").all()
            ]
        
