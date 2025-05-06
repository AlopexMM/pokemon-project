import re

from playwright.sync_api import Page
from playwright.sync_api import expect
from ..test_fixtures.context_for_tests import card_manager
from ..test_fixtures.context_for_tests import pokemon_config
from ..page_objects.card_manager_page import CardManager

def test_has_h1_title(card_manager: CardManager):
    
    # Derificamos que se encuentre en un h1 el texto "Creador de cartas Pokemon"
    expect(card_manager.title_heading).to_have_text("Creador de cartas Pokemon")
    # expect(page.get_by_role("heading", name="Creador de cartas Pokemon")).to_be_visible()

def test_create_card(card_manager: CardManager):

    # Seleccionamos un pokemon
    card_manager.select_pokemon()

    # Ingresamos un nombre al pokemon
    card_manager.name_input.fill("Playwright")

    # Ingresamos el valor de la vida
    card_manager.life_input.fill("100")
    
    # Ingresamos el valor de la velocidad
    card_manager.speed_input.fill("50")
    
    # Ingresamos el valor del ataque
    card_manager.atack_input.fill("60")
    
    # Ingresamos el valor de la defensa
    card_manager.defense_input.fill("10")

    # Presionamos el boton crear Pokemon
    card_manager.create_card.click()

    # Verificamos que se haya creado la carta
    expect(card_manager.card_created("Playwright")).to_be_visible()

def test_delete_card(pokemon_config: Page):
    
    # Corremos la generación de la carta
    card_manager = CardManager(pokemon_config)
    test_create_card(card_manager)

    # Ubicamos la carta y presionamos el boton borrar
    card_manager.card_created_delete("Playwright")

    # Verificamos que no se encuentre mas la carta
    expect(card_manager.card_created("Playwright")).not_to_be_visible()