import reflex as rx
from coras import style
from coras.state import State
from typing import List


def panel(data: List):
    return rx.box(
        rx.text(data)
        # rx.text(data["last_name"])
        # rx.text(State.form_data["last_name"])
    )

def insert():
    return rx.vstack( 
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Categoria",
                    id="category",
                ),
                rx.input(
                    placeholder="Contrario", id="enemy"
                ),
                rx.input(
                    placeholder="Dia", id="day"
                ),
                rx.input(
                    placeholder="Hora", id="hour"
                ),
                rx.input(
                    placeholder="Pabellon", id="poli"
                ),
                rx.hstack(
                    rx.switch("Local", id="local"),
                    rx.switch("Descansa", id="rest"),
                ),

                rx.button("Submit", type_="submit", on_click=rx.console_log(State.names)),
            ),
            on_submit=State.add_partidos,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.box(
            rx.foreach(
                State.names,
                panel
            )
        ),
        margin="2em",
        
        # rx.text(State.form_data["first_name"]),
        # rx.text(State.form_data["last_name"])
    )    