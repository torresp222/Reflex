"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from .components.navbar import navbar
from .components.partidos import buscador, tarjeta_partido, buscador2
from .components.inst import insert
from .components.next_jornada import next_jor
from .components.table import table_ataque, table_defensa
from .components.up_stats import update_est, button_change
from .components.up_match import update_hour
from .backend.api import api_test, update_res_match, update_hour_match
from .models import Partidos
# from coras import style
from .style import style
from .state import State

import reflex as rx

# class State(rx.State):
#     pass

def index():
    return rx.box(
        navbar(),
        # buscador2(),
        # rx.box(
        #     rx.text(
        #         State.partidos
        #     )
        # )
        # rx.button(
        #     "Click Me!",
        #     on_click=State.add_partidos,
        # )
        )
    
def partidos():
    return rx.box(
        navbar(),
        buscador(),
        next_jor(),
        rx.center(rx.heading("Calendario Completo", size="lg"), margin_top="5em", margin_bottom="3em"),
        rx.divider(border_color="black"),
        tarjeta_partido()
        )

def stats():
    return rx.box(
        navbar(),
        rx.center(rx.heading("Ataque", size="2xl"), margin_top="2em"),
        table_ataque(),
        rx.center(rx.heading("Defensa", size="2xl"), margin_top="2em"),
        table_defensa()
    )

def actualizar_stats():
    return rx.box(
            navbar(),
            button_change(),
            update_est()
        )

def insertar():
    return rx.fragment(
        navbar(),
        insert()
        )

def actualizar_partidos():
    return rx.box(
         navbar(),
         update_hour()
    )




# Add state and page to the app.
app = rx.App()
app.add_page(index, title = "Bmcoras")
app.add_page(partidos, route="/partidos", title = "Bmcoras")
app.add_page(stats, route="/stats", title = "Bmcoras")
app.add_page(insertar, route="/inst", title = "Bmcoras")
app.add_page(actualizar_stats, route="/update-stats", title = "Bmcoras")
app.add_page(actualizar_partidos, route="/update-matches", title = "Bmcoras")

app.api.add_api_route("/items/{item_id}", api_test)
app.api.add_api_route("/resultado/{category}/{enemy}/{day}/{res}/{enemy_res}", update_res_match)
app.api.add_api_route("/hora/{category}/{enemy}/{day}/{hour}", update_hour_match)


app.compile()
