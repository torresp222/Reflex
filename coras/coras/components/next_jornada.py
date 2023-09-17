import reflex as rx
from coras import style
from coras.state import State
from typing import List


def next_jor():
    return rx.card(
            rx.text(
                rx.center(
                    rx.cond(
                        State.rest,
                        rx.text(" "),
                        rx.box(
                            rx.cond(
                                State.local,
                                rx.hstack(
                                    # Imagen del Logo del equipo en concreto
                                    rx.image(src="/bmcoras-logo.jpg", width="20px", margin="0.5em"),
                                    rx.text(State.selected),  
                                    # rx.text(State.res, as_="b"), 
                                    rx.text("vs") , 
                                    # rx.text(State.enemy_res, as_="b"),  
                                    rx.text(State.enemy_one),
                                    rx.image(src="/" + State.enemy_one + ".jpg", width="20px", margin="0.5em"),
                                ),
                                rx.hstack(
                                    # Imagen del Logo del equipo en concreto
                                    rx.image(src="/" + State.enemy_one + ".jpg", width="20px", margin="0.5em"),
                                    rx.text(State.enemy_one),  
                                    # rx.text(State.enemy_res, as_="b"), 
                                    rx.text("vs") , 
                                    # rx.text(State.res, as_="b"),  
                                    rx.text(State.selected),
                                    rx.image(src="/bmcoras-logo.jpg", width="20px", margin="0.5em"),
                                )
                            )    
                        )
                    )
                ),
                
                rx.center(
                    rx.cond(
                        State.rest,
                        rx.text(State.next_match),
                        rx.text(State.poli + " " + State.hour)
                    )
                ),
            ),
            header=rx.center(rx.vstack(rx.heading("SIGUIENTE JORNADA", size="lg"),rx.heading(State.selected, size="lg"), rx.cond(State.rest,rx.heading("Descansa"),rx.heading(State.next_match)), size="2em")),
            # footer=rx.center(rx.heading("Footer", size="sm"), align="center"),
            margin_top="2em",
            border_radius="10px",
            box_shadow="0px 2px 10px rgba(0, 0, 0, 0.2)",
            opacity=State.opa, #/* La tarjeta estará inicialmente oculta */
            transform=State.trsl, #/* La tarjeta estará ligeramente desplazada hacia abajo */
            transition="opacity 0.5s ease, transform 0.5s ease"
            ) 