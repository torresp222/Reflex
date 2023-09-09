import reflex as rx

class Partidos(rx.Model, table=True):
    category: str
    enemy: str
    day: str
    hour: str
    local: bool
    rest: bool = False
    poli : str = "Pabellon"
    res: str = " "
    enemy_res: str = " "


class Stats(rx.Model, table=True):
    category: str
    player: str
    matches: int
    shots: int
    scores: int
    effy_shots: str 
    penals : int 
    steals: int
    stops: int
    goals_in: int
    effy_stops: str
    keeper: bool    