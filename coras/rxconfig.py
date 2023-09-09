import reflex as rx

class CorasConfig(rx.Config):
    pass

config = CorasConfig(
    app_name="coras",
    db_url="sqlite:///coras.db",
)