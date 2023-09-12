import reflex as rx
from .state import State
from typing import List, Dict
from .models import Stats

class ChildState1(State):
    datas: Dict[int, str] = {}
    team_list: dict = {}
    player_name: List = []
    player_matches: List = []
    player_shots: List = []
    player_goals: List = []
    player_effy: List = []
    player_penals: List = []

    stats: str
    data_ataque: List[List] = []
    """ data_ataque: List = [
        ["Asier Dueñas", "10", "20", "10", "50%", "5"],
        ["Daniel Azofra", "10", "35", "25", "70%", "1"],
    ] """
    columns_ataque: List[str] = ["Name", "Partidos Jugados", "Lanzamientos", "Goles", "Eficacia de Goles", "Penaltis provocados"]

    data_defensa: List = [
        ["Nacho Fernandez", "2", "5", "0","0","0%"],
        ["Sergio Herrero", "0", "0", "0","30","75%"],
    ]
    columns_defensa: List[str] = ["Name", "Bloqueos", "Robos de balón", "Faltas en ataque", "Paradas", "Porcentaje de Paradas"]
    

    def give_team(self):
        if self.data_ataque:
            self.data_ataque = []

        with rx.session() as session:
            self.team_list = (
                session.query(Stats).all()
            )

        #print(self.team_list)
        self.player_name = [self.stats.player for self.stats in self.team_list]
        self.player_matches = [self.stats.matches for self.stats in self.team_list]
        self.player_shots = [self.stats.shots for self.stats in self.team_list]
        self.player_goals = [self.stats.scores for self.stats in self.team_list]
        self.player_effy = [self.stats.effy_shots for self.stats in self.team_list]
        self.player_penals = [self.stats.penals for self.stats in self.team_list]

        print(len(self.player_name))
        
        self.datas = {}
        dat: List = []
        i = 0
        for data in self.player_name:
            print(data)
            j =0 
            #print(self.data_ataque[i][4])
            #dat = [j for j in range(i)] 
            dat = [data, str(self.player_matches[i]), str(self.player_shots[i]), str(self.player_goals[i]), self.player_effy[i], str(self.player_penals[i])]
            self.data_ataque.append([])
            self.data_ataque[i].append(dat)
           # print(str(self.data_ataque[i][0][4]) + "  aaaa")
            if self.player_shots[i]<=0:
                pass
            else:
                porcen = (self.player_goals[i] / self.player_shots[i]) * 100 
                self.data_ataque[i][0][4] = str(round(porcen)) + "%"
                # print(self.data_ataque[i])
            i += 1

        for j in range(len(self.data_ataque)):
            self.data_ataque[j-1] = self.data_ataque[j-1][0]
        print(self.data_ataque)

    def give_team_stats(self):
        with rx.session() as session:
            self.team_list = (
                session.query(Stats).all()
            )

        #print(self.team_list)
        self.player_name = [self.stats.player for self.stats in self.team_list]
        self.player_matches = [self.stats.matches for self.stats in self.team_list]
        self.player_shots = [self.stats.shots for self.stats in self.team_list]
        self.player_goals = [self.stats.scores for self.stats in self.team_list]
        self.player_effy = [self.stats.effy_shots for self.stats in self.team_list]
        self.player_penals = [self.stats.penals for self.stats in self.team_list]

        print(len(self.player_name))
        
        self.datas = {}
        i = 0
        for data in self.player_name:
            #print(self.data_ataque[i][4])
            #dat = [j for j in range(i)] 
            self.datas[i] = [data, str(self.player_matches[i]), str(self.player_shots[i]), str(self.player_goals[i]), self.player_effy[i], str(self.player_penals[i])]
            i += 1
        print(self.datas)

    def increment(self, item, resource):
        print(self.datas[int(item)][0])
        print(str(self.datas[int(item)][2]) + " mas uno")
        self.datas[int(item)][resource] = str(int(self.datas[int(item)][resource]) + 1)
        with rx.session() as session:
            row = (
                session.query(Stats)
                .filter(Stats.player.contains(self.datas[int(item)][0]))
                .first()
            )
            # partido.update()
            print(row)
            if resource == 2:
                row.shots = self.datas[int(item)][resource]
            elif resource == 3:
                row.scores = self.datas[int(item)][resource]
            else:
                row.penals = self.datas[int(item)][resource]
            session.commit()
    
    def decrement(self, item, resource):
        print(type(item))
        print(str(item))
        # print(str(self.datas[int(item)][2]) + " menos uno")
        print("Abajo es el resource")
        print(self.datas[int(item)][resource] + " Holaaaa")
        self.datas[int(item)][resource] = str(int(self.datas[int(item)][resource]) - 1) 


