from playwright.sync_api import Page, expect, Selectors

def test_has_title(page: Page):
    
    page.goto("http://localhost:8080")

    # Con expect verificamos que se cumpla una condición
    pokemon_title = page.frame_locator(".title").get_by_text("Pokemon")
    expect(pokemon_title).to_have_text("Creador de cartas Pokemon")