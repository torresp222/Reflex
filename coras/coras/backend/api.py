import reflex as rx
from coras.models import Partidos

async def api_test(item_id: int):
    return {"my_result": item_id}


async def update_res_match(category: str, enemy: str, day: str, res: str, enemy_res: str):

    try:
        with rx.session() as session:
            partido = (
                session.query(Partidos)
                .filter(Partidos.category.contains(category), Partidos.enemy.contains(enemy), Partidos.day.contains(day))
                .first()
            )
            # partido.update()
            print(partido)
            partido.res = res
            partido.enemy_res = enemy_res
            session.commit()
    except Exception as e:
        print(e)

    return {
        "categoria": partido.category,
        "contrario": partido.enemy,
        "Dia": partido.day,
        "Resultado": partido.res,
        "Resultado contrario": partido.enemy_res
        }

async def update_hour_match(category: str, enemy: str, day: str, hour: str):

    try:
        with rx.session() as session:
            partido = (
                session.query(Partidos)
                .filter(Partidos.category.contains(category), Partidos.enemy.contains(enemy), Partidos.day.contains(day))
                .first()
            )
            # partido.update()
            print(partido)
            partido.hour = hour
            session.commit()
    except Exception as e:
        print(e)

    return {
        "categoria": partido.category,
        "contrario": partido.enemy,
        "Dia": partido.day,
        "Resultado": partido.hour
        }
