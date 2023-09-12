import reflex as rx
from coras import style
from coras.state import State
from typing import List

def update_hour():
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

                rx.button("Submit", type_="submit", on_click=rx.console_log(State.names)),
            ),
            on_submit=State.update_hour_one_match,
        ),
        margin="2em",
        
        # rx.text(State.form_data["first_name"]),
        # rx.text(State.form_data["last_name"])
        )

def update_poli():
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
                    placeholder="Pabellon", id="poli"
                ),

                rx.button("Submit", type_="submit", on_click=rx.console_log(State.names)),
            ),
            on_submit=State.update_poli_one_match,
        ),
        margin="2em",
        
        )

def update_day():
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
                    placeholder="Dia Previo", id="day"
                ),
                rx.input(
                    placeholder="Dia Actualizado", id="day_act"
                ),

                rx.button("Submit", type_="submit", on_click=rx.console_log(State.names)),
            ),
            on_submit=State.update_day_one_match,
        ),
        margin="2em",
        
        )