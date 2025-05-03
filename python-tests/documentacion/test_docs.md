## Video 1

### Comencemos con los Tests

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

#### Crear tarjeta Pokemon

```python
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
```

#### Borrar tarjeta Pokemon

```python
def test_delete_card(page: Page):
    
    # Corremos la generación de la carta
    test_create_card(page)

    # Ubicamos la carta y presionamos el boton borrar
    page.locator("//div[contains(@class, \"card\")]/div[@class=\"name\"]/h3[text()=\"Playwright\"]/parent::div/parent::div/div/button").click()

    # Verificamos que no se encuentre mas la carta
    expect(page.get_by_alt_text("Playwright")).not_to_be_visible()
```

## Video 2

### Usando Fixtures con pytest

Que es un fixture? 

Es una funcionalidad que nos permite darle un contexto a la función que se va a ejecutar en este caso el test.

```python
```