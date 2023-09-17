import reflex as rx
from coras import style
from coras.state import State
from typing import List


def buscador():
    return rx.box(
        rx.select(
            State.options,
            placeholder="Categoría",
            # is_multi=True,
            on_change=State.set_selected,
            on_click=State.give_enemy_team,
            # on_mouse_down=State.give_enemy_team,
            #on_mouse_down=State.transition,
            # close_menu_on_select=False,
            color_schemes="twitter"
        ),
        width="10em",
        margin_top="1em"
    )

def buscador2():
    return rx.box(
        rx.select(
            State.options,
            placeholder="Categoría",
            # is_multi=True,
            on_change=State.set_selected,
            on_click=State.give_enemy_team,
            # close_menu_on_select=False,
            color_schemes="twitter"
        ),
        width="10em",
        margin_top="1em"
    )

def get_tarjeta_partido(match: List):
    # key, value = key_value
    # cat = match
    # en = match[i].enemy

    return rx.card(
            rx.text(
                rx.center(
                    rx.cond(
                        # Variable Descansa. Si descansa no se añade texto
                        match[1][4],
                        rx.text(" "),
                        rx.fragment(
                            rx.cond(
                                # Variable Local. Si es local aparece a la izquierda el equipo de coras, si no, a la derecha.
                                match[1][3],
                                rx.hstack(
                                    # Imagen del Logo del equipo en concreto
                                    rx.image(src="/bmcoras-logo.jpg", width="20px", margin="0.5em"),
                                    rx.text(State.selected),  
                                    rx.text(match[1][6], as_="b"), 
                                    rx.text("-") , 
                                    rx.text(match[1][7], as_="b"),  
                                    rx.text( match[1][0]),
                                    rx.image(src="/" +  match[1][0] + ".jpg", width="20px", margin="0.5em"),
                                ),
                                rx.hstack(
                                    # Imagen del Logo del equipo en concreto
                                    rx.image(src="/" +  match[1][0] + ".jpg", width="20px", margin="0.5em"),
                                    rx.text(match[1][0]),  
                                    rx.text(match[1][7], as_="b"), 
                                    rx.text("-") , 
                                    rx.text(match[1][6], as_="b"),  
                                    rx.text(State.selected),
                                    rx.image(src="/bmcoras-logo.jpg", width="20px", margin="0.5em"),
                                ), 
                            )
                        ),
                    ),
                    display="flex"
                ),
                rx.center(
                    rx.cond(
                        # Variable Descansa
                        match[1][4],
                        # Variable que lleva el día de partido
                        rx.text(match[1][1]),
                        # Varible que dice el Pabellon. Y variable que dice la hora del partido
                        rx.text(match[1][5] + " " + match[1][2]),
                    )    
                ),
            ),
            header=rx.center(rx.vstack(rx.heading(State.selected, size="lg"), rx.cond(match[1][4], rx.heading("Descansa"),rx.heading(match[1][1])),font_size="1em")),
            # footer=rx.center(rx.heading("Footer", size="sm"), align="center"),
            margin_top="2em",
            border_radius="10px",
            box_shadow="0px 2px 10px rgba(0, 0, 0, 0.2)",
            opacity=State.opa, #/* La tarjeta estará inicialmente oculta */
            transform=State.trsl, #/* La tarjeta estará ligeramente desplazada hacia abajo */
            transition="opacity 0.5s ease, transform 0.5s ease"
            ) 

# rx.box(
#             rx.text(match[1][0])
#             )
    

    # return rx.card(
    #         rx.text(
    #             rx.center(
    #                 # Imagen del Logo del equipo en concreto
    #                 rx.image(src="/bmcoras-logo.jpg", width="20px", margin="0.5em"),State.selected + " vs " +
    #                             # Imagen del Logo del equipo en concreto 
    #                 enemy,rx.image(src="/bmcoras-logo.jpg", width="20px", margin="0.5em"),
    #                 display="flex",
    #             ),
    #             rx.center(rx.text("Pabellon y horas")),
    #         ),
    #         header=rx.center(rx.vstack(rx.heading(State.selected, size="lg"), rx.heading("Dia"), size="2em")),
    #         # footer=rx.center(rx.heading("Footer", size="sm"), align="center"),
    #         margin_top="2em",
    #         border_radius="10px",
    #         box_shadow="0px 2px 10px rgba(0, 0, 0, 0.2)",
    #         opacity=State.opa, #/* La tarjeta estará inicialmente oculta */
    #         transform=State.trsl, #/* La tarjeta estará ligeramente desplazada hacia abajo */
    #         transition="opacity 0.5s ease, transform 0.5s ease"
    #         ) 

def tarjeta_partido():
    # iterable_data = len(State.enemy_team)
    # print(State.enemy_team[0])
    return rx.box(
            rx.foreach(
                State.dict_of_lists,
                get_tarjeta_partido
                # lambda enemy, i: get_tarjeta_partido(enemy, i)
            )
            # class_name="card-container"
    )