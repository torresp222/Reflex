import reflex as rx
from coras import style
from coras.state import State
from coras.child_one import ChildState1
from typing import List

# def buscador2():
#     return rx.box(
#         rx.select(
#             ChildState1.options,
#             placeholder="Categoría",
#             # is_multi=True,
#             #on_change=ChildState1.set_selected,
#             on_click=ChildState1.give_team,
#             # close_menu_on_select=False,
#             color_schemes="twitter"
#         ),
#         width="10em",
#         margin_top="1em"
#     )

def button_change():
    return rx.button(
            "Change", on_click=ChildState1.give_team_stats
    )

def update_stats_player(name: List):
    # print("------\n"+ name[1])
    return rx.box(
            rx.hstack(
                rx.text(name[1][0]),
                ### Lanzamientos
                rx.box(rx.button(
                    rx.icon(tag="minus"),
                    bg="#fef2f2",
                    color="#b91c1c",
                    border_radius="lg",
                    width="5%",
                    height="5%",
                    on_click=lambda: ChildState1.decrement(
                        name[0], 2
                    ),
                ), padding_top="1em", padding_left="1em", margin_left="2em"),                   
                rx.vstack(
                    rx.heading("Lanzamientos", size="sm"),
                    rx.text(
                        # Lanzamientos
                        name[1][2],
                        padding_bottom="0.5em",
                    )
                ),
                rx.box(rx.button(
                    rx.icon(tag="add"),
                    bg="#ecfdf5",
                    color="#047857",
                    border_radius="lg",
                    width="5%",
                    height="5%",
                    on_click=lambda: ChildState1.increment(
                        name[0], 2
                    )
                ), padding_top="1em", padding_right="1em"),
            ### GOLES
                rx.box(rx.button(
                    rx.icon(tag="minus"),
                    bg="#fef2f2",
                    color="#b91c1c",
                    border_radius="lg",
                    width="5%",
                    height="5%",
                    on_click=lambda: ChildState1.decrement(
                        name[0], 3
                    ),
                ), padding_top="1em", padding_left="1em", margin_left="2em"),                   
                rx.vstack(
                    rx.heading("Goles", size="sm"),
                    rx.text(
                        # Goles
                        name[1][3],
                        padding_bottom="0.5em",
                    ),
                ),
                rx.box(rx.button(
                    rx.icon(tag="add"),
                    bg="#ecfdf5",
                    color="#047857",
                    border_radius="lg",
                    width="5%",
                    height="5%",
                    on_click=lambda: ChildState1.increment(
                        name[0], 3
                    )
                ), padding_top="1em", padding_right="1em",),

                ### Penaltis Provocados                  
                rx.vstack(
                    rx.heading("Penaltis", size="sm"),
                    rx.text(
                        # Penaltis Provocados
                        name[1][5],
                        padding_bottom="0.5em",
                    ),
                ),
                rx.box(rx.button(
                    rx.icon(tag="add"),
                    bg="#ecfdf5",
                    color="#047857",
                    border_radius="lg",
                    width="5%",
                    height="5%",
                    on_click=lambda: ChildState1.increment(
                        name[0], 5
                    )
                ), padding_top="1em", padding_right="1em",),
            ),
            rx.divider(border_color="black"),
            margin_top="2em",
            
        )


def update_est():
    return rx.box(
            rx.foreach(
                ChildState1.datas,
                update_stats_player
                # lambda enemy, i: get_tarjeta_partido(enemy, i)
            ),
            # class_name="card-container"
    )