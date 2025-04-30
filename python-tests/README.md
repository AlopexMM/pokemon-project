# Playwright tests

Como requerimiento tenemos que tener instalado python 3.8+.

Ahora vamos a preparar el entorno con los siguientes comandos:

```powershell
python -m venv venv
```

Activamos el entorno e instalamos con pip Playwright.

```powershell
./venv/Scripts/activate

pip install pytest-playwright
```

Ahora instalemos los buscadores necesarios para el correcto funcionamiento de **Playwright**.

```powershell
playwright install
```

Si necesitamos actualizar a la ultima versión debemos utilizar el siguiente comando

```powershell
pip install pytest-playwright playwright -U
```

# Documentación para los tests
![docs](./documentacion/test_docs.md)