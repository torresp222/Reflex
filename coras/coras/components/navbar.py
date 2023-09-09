import reflex as rx
from coras import style

def navbar():
    return rx.flex(
        rx.box(
            rx.link(rx.image(src="/bmcoras-logo.jpg", width="60px", margin="0.5em"), href="/")
        ),
        rx.center(
            rx.list(
                rx.list_item(rx.link(rx.button("Partidos", style=style.button_nav_style), href="/partidos"), margin="0.5em"),
                rx.list_item(rx.link(rx.button("Clasificaciones", style=style.button_nav_style)), margin="0.5em"),
                rx.list_item(rx.link(rx.button("Estadísticas", style=style.button_nav_style), href="/stats"), margin="0.5em"),
                display="flex"
            ),
            margin_right="10em",
            
        ),
        justify_content="space-between",
        background_image="linear-gradient(to right, #3498db, #e74c3c)"
    )