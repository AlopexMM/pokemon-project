import re

from playwright.sync_api import Page
from playwright.sync_api import expect
from test_fixtures.context_for_tests import pokemon_config

def test_has_h1_title(pokemon_config: Page):

    # Derificamos que se encuentre en un h1 el texto "Creador de cartas Pokemon"
    expect(pokemon_config.locator("//div[contains(@class, \"title\")]/h1")).to_have_text("Creador de cartas Pokemon")
    # expect(page.get_by_role("heading", name="Creador de cartas Pokemon")).to_be_visible()

def test_create_card(pokemon_config: Page):

    # Seleccionamos un pokemon
    
    pokemon_config.get_by_alt_text("bulbasaur").click()

    # Ingresamos un nombre al pokemon
    pokemon_config.get_by_role("textbox", name="Nombre *").fill("Playwright")

    # Ingresamos el valor de la vida
    pokemon_config.get_by_role("spinbutton", name="Vida 1-100 *").fill("100")
    
    # Ingresamos el valor de la velocidad
    pokemon_config.get_by_role("spinbutton", name="Velocidad 1-100 *").fill("50")
    
    # Ingresamos el valor del ataque
    pokemon_config.get_by_role("spinbutton", name="Ataque 1-100 *").fill("60")
    
    # Ingresamos el valor de la defensa
    pokemon_config.get_by_role("spinbutton", name="Defensa 1-100 *").fill("10")

    # Presionamos el boton crear Pokemon
    pokemon_config.get_by_role("button", name="Crear Pokemon").click()

    # Verificamos que se haya creado la carta
    expect(pokemon_config.get_by_alt_text("Playwright")).to_be_visible()

def test_delete_card(pokemon_config: Page):
    
    # Corremos la generación de la carta
    test_create_card(pokemon_config)

    # Ubicamos la carta y presionamos el boton borrar
    pokemon_config.locator("//div[contains(@class, \"card\")]/div[@class=\"name\"]/h3[text()=\"Playwright\"]/parent::div/parent::div/div/button").click()

    # Verificamos que no se encuentre mas la carta
    expect(pokemon_config.get_by_alt_text("Playwright")).not_to_be_visible()