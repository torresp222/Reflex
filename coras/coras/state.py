import reflex as rx
from typing import List, Dict
from .models import Partidos
from .backend.api import update_hour_match
import asyncio
import json
from datetime import datetime


# class Teams(rx.Base):
#     enemy_team: List[str]

class State(rx.State):
    # options: List[str] = ["Infantil B", "Infantil A", "Cadete B", "Segunda Nacional Masc", "Cadete A"]
    options: List[str] = ["Infantil A", "Segunda Nacional Masc"]
    # selected: List[str] = []
    selected: str

    enemy_match: List = []
    day_match: List = []
    hour_match: List = []
    local_match: List[bool] = []
    rest_match: List[bool] = []
    poli_match: List = []
    res_match: List = []
    enemy_res_match: List = []

    next_match: str
    enemy_one: str
    hour: str
    poli: str
    local: bool
    rest: bool
    res: str
    enemy_res: str

    form_data: dict = {}
    names: List = []
    partidos_list: dict = {}
    partido: str
    name: List[str] = []
    day = str
    dict_of_lists: Dict[int, str] = {}
    opa = "1"
    trsl = "translateY(0)"
    
    def add_partidos(self, form_data: dict):
        name = form_data["category"] + " " + form_data["enemy"] + " " + form_data["day"] + " " + form_data["hour"] + " " + str(form_data["local"]) + " " + str(form_data["rest"]) + " " + form_data["poli"]
        self.names.append(name)
        name = ""
        with rx.session() as session:
            session.add(
                Partidos(
                    category=form_data["category"],
                    enemy=form_data["enemy"],
                    day=form_data["day"],
                    hour=form_data["hour"],
                    local=form_data["local"],
                    rest=form_data["rest"],
                    poli=form_data["poli"],
                    res= " ",
                    enemy_res=" "
                )
            )

            session.commit()  

    #@rx.var
    def give_enemy_team(self):
        self.opa = "1"
        self.trsl = "translateY(0)"

        with rx.session() as session:
            self.partidos_list = (
                session.query(Partidos)
                .filter(Partidos.category.contains(self.selected))
                .all()
            )

        print(self.partidos_list)
        print("-------------------------")   
        # self.enemy_match = [self.partido.enemy for self.partido in self.partidos_list]
        self.day_match = [self.partido.day for self.partido in self.partidos_list]
        self.day_match, self.enemy_match, self.res_match, self.enemy_res_match, self.local_match, self.rest_match, self.hour_match, self.poli_match  = self.sort_date(self.day_match)
 
        print("Entro en next funn")
        self.next_match,self.enemy_one, self.local, self.poli, self.hour, self.rest, self.res, self.enemy_res = self.next_weekend(self.day_match)

        # 
        print("Salgo de next")
        i = 0
        self.dict_of_lists = {}
        for self.enemy in self.enemy_match:
            self.dict_of_lists[i] = [self.enemy_match[i], self.day_match[i], self.hour_match[i], self.local_match[i], self.rest_match[i], self.poli_match[i], self.res_match[i], self.enemy_res_match[i]]
            print(self.dict_of_lists[i])
            i += 1
        
        print(self.dict_of_lists)

    async def transition(self):
        self.opa = "0"
        self.trsl = "translateY(20px)"
        yield

        await asyncio.sleep(0.5)


    def sort_date(self, list_date: List) -> List:

        # Convert date strings to datetime objects for sorting
        formatted_dates = [datetime.strptime(date, '%d-%m-%Y') for date in list_date]

        # Sort the datetime objects in descending order (most recent to farthest)
        sorted_dates = sorted(formatted_dates, reverse=False)

        # Convert sorted datetime objects back to date strings
        sorted_date_strings = [date.strftime('%d-%m-%Y') for date in sorted_dates]
        teams = []
        res = []
        enemy_res = []
        local = []
        rest = []
        hour = []
        poli = []
        # i = 0
        for date in sorted_date_strings:
            with rx.session() as session:
                team = (
                    session.query(Partidos)
                    .filter(Partidos.day.contains(date), Partidos.category.contains(self.selected))
                    .first()
                )

            teams.append(team.enemy)
            res.append(team.res)
            enemy_res.append(team.enemy_res)
            local.append(team.local)
            rest.append(team.rest)
            hour.append(team.hour)
            poli.append(team.poli)
            # print(teams)

        # next = State.next_weekend(sorted_date_strings)
        # print(sorted_date_strings)
        return sorted_date_strings, teams, res, enemy_res, local, rest, hour, poli
    

    def next_weekend(self, sorted_dates: List) -> str:
        # Convert date strings to datetime objects

        date_objects = [datetime.strptime(date, '%d-%m-%Y') for date in sorted_dates]
        # Get today's date
        today = datetime.today()
        # Find the first date that is greater than or equal to today
        next_date = None
        for date in date_objects:
            if date >= today:
                next_date = date
                break

        if next_date:
            next_date_str = next_date.strftime('%d-%m-%Y')
            print(f"The next date from today is: {next_date_str}")
        else:
            print("There are no future dates in the list.")
        
        with rx.session() as session:
            match = (
                session.query(Partidos)
                .filter(Partidos.day.contains(next_date_str))
                .first()
            )

        print(type(match.enemy))

        return next_date_str, match.enemy, match.local, match.poli, match.hour, match.rest, match.res, match.enemy_res
    

    async def update_hour_one_match(self, form_data: dict):
        await update_hour_match(form_data["category"],form_data["enemy"],form_data["day"],form_data["hour"])
 