import pytest

from playwright.sync_api import Playwright

@pytest.fixture(scope="function", autouse=True)
def pokemon_config(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("automation-id")
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    
    # Vamos a la pagina del buscador
    page.goto("http://localhost:8080")

    return page