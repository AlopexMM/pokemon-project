from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from prefab_ui.app import PrefabApp
from prefab_ui.actions import Fetch, SetState
from prefab_ui.components import (
    Badge,
    Column,
    Card,
    CardContent,
    DataTable,
    DataTableColumn,
    Text,
)
from prefab_ui.rx import RESULT, Rx, STATE

ui_router = APIRouter()

@ui_router.get(
    "/",
    response_class=HTMLResponse
)
def page():
    Fetch(
        "/api/all",
        method="GET",
        on_success=SetState("pokemons", RESULT)
    )
    with Column() as view:
        DataTable(
            columns=[
                DataTableColumn(key="uid", header="ID"),
                DataTableColumn(key="name", header="Name"),
                DataTableColumn(key="elements", header="Type")
            ],
            rows=STATE.pokemons,
            paginated=True,
            page_size=10,
            search=True
        )
    return HTMLResponse(
        PrefabApp(
            title="Pokedex app",
            view=view,
            ).html()
    )
