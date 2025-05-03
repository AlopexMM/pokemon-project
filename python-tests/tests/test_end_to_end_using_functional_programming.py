import re
from playwright.sync_api import Page, expect, Selectors

def test_has_title(page: Page):
    
    page.goto("http://localhost:8080")

    # Con expect verificamos que se cumpla una condición de que el titulo posee la palabra "Pokemon"
    expect(page).to_have_title(re.compile("^Pokemon"))

def test_has_h1_title(page: Page):

    page.goto("http://localhost:8080")

    # Derificamos que se encuentre en un h1 el texto "Creador de cartas Pokemon"
    expect(page.locator("//div[contains(@class, \"title\")]/h1")).to_have_text("Creador de cartas Pokemon")
    # expect(page.get_by_role("heading", name="Creador de cartas Pokemon")).to_be_visible()

def test_create_card(page: Page):

    # Nos dirigimos a la pagina web
    page.goto("http://localhost:8080")

    # Seleccionamos un pokemon
    page.get_by_alt_text("bulbasaur").click()

    # Ingresamos un nombre al pokemon
    page.get_by_role("textbox", name="Nombre *").fill("Playwright")

    # Ingresamos el valor de la vida
    page.get_by_role("spinbutton", name="Vida 1-100 *").fill("100")
    
    # Ingresamos el valor de la velocidad
    page.get_by_role("spinbutton", name="Velocidad 1-100 *").fill("50")
    
    # Ingresamos el valor del ataque
    page.get_by_role("spinbutton", name="Ataque 1-100 *").fill("60")
    
    # Ingresamos el valor de la defensa
    page.get_by_role("spinbutton", name="Defensa 1-100 *").fill("10")

    # Presionamos el boton crear Pokemon
    page.get_by_role("button", name="Crear Pokemon").click()

    # Verificamos que se haya creado la carta
    expect(page.get_by_alt_text("Playwright")).to_be_visible()