"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from chatapp import style
from chatapp.state import State

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em",
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )

def dark_mode() -> rx.Component:
    return rx.button(
        rx.icon(tag="moon"),
        on_click=rx.toggle_color_mode,
        position="absolute",
        top="0px",
        right="10px"
    ) 


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def index() -> rx.Component:
    return rx.container(
        dark_mode(),
        chat(),
        action_bar(),
        )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
