import reflex as rx
from coras import style
from coras.state import State
from coras.child_one import ChildState1
from typing import List

def table_ataque():
    return rx.center(rx.box(
            
                rx.data_table(
                    data=ChildState1.data_ataque,
                    columns=ChildState1.columns_ataque,
                    search=True,
                    sort=True,
                    resizable=True,
                ),
                # display="center",
                width="80%",
                margin_top="1em"
            
        ) )

def table_defensa():
    return rx.center(rx.box(
            
                rx.data_table(
                    data=ChildState1.data_defensa,
                    columns=ChildState1.columns_defensa,
                    search=True,
                    sort=True,
                    resizable=True,
                ),
                # display="center",
                width="80%",
                margin_top="1em"
            
        ) )


def update_stats_player(name):
    return rx.box(
            rx.text(name)
    )


def update_est():
    return rx.box(
            rx.foreach(
                ChildState1.data_ataque,
                update_stats_player
                # lambda enemy, i: get_tarjeta_partido(enemy, i)
            )
            # class_name="card-container"
    )