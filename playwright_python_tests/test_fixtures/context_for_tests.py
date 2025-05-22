import pytest

from playwright.sync_api import Playwright
from playwright.sync_api import Page
from ..page_objects.card_manager_page import CardManager

@pytest.fixture(scope="function")
def pokemon_config(playwright: Playwright) -> Page:
    playwright.selectors.set_test_id_attribute("automation-id")
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    
    # Vamos a la pagina del buscador
    page.goto("http://localhost:5173/")

    return page

@pytest.fixture(scope="function")
def card_manager(pokemon_config: Page) -> CardManager:
    return CardManager(pokemon_config)