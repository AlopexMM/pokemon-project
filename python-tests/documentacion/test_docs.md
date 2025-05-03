# Comencemos con los Tests

Si corremos la aplicación y nos dirigimos a http://localhost:8080 y abrimos la consola de inspección, con boton derecho sobre la pagina y vamos a inspect o inspeccionar dependiendo 

![app_inspect](./imagenes/app_inpect.png)

Con nuestro primer script navegamos al buscador y checkeamos que el titulo que en el titulo se encuentre la palabra "Pokemon" y que se encuentre el texto "Creador de cartas Pokemon".

![inspect_title](./imagenes/inspect_title.png)

```python
def test_has_title(page: Page):
    
    page.goto("http://localhost:8080")

    # Con expect verificamos que se cumpla una condición de que el titulo posee la palabra "Pokemon"
    expect(page).to_have_title(re.compile("^Pokemon"))

def test_has_h1_title(page: Page):

    page.goto("http://localhost:8080")

    # Derificamos que se encuentre en un h1 el texto "Creador de cartas Pokemon"
    expect(page.locator("//div[contains(@class, \"title\")]/h1")).to_have_text("Creador de cartas Pokemon")
    # expect(page.get_by_role("heading", name="Creador de cartas Pokemon")).to_be_visible()
```

Bien veamos otros dos test mas creando un E2E de la pagina para la creación, y borrado de tarjetas.

```python

```