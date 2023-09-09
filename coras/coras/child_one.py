import reflex as rx
from .state import State
from typing import List, Dict

class ChildState1(State):
    datas: Dict[int, str] = {}
    data_ataque: List = [
        ["Asier Dueñas", "10", "20", "10", "50%", "5"],
        ["Daniel Azofra", "10", "35", "25", "70%", "1"],
    ]
    columns_ataque: List[str] = ["Name", "Partidos Jugados", "Lanzamientos", "Goles", "Eficacia de Goles", "Penaltis provocados"]

    data_defensa: List = [
        ["Nacho Fernandez", "2", "5", "0","0","0%"],
        ["Sergio Herrero", "0", "0", "0","30","75%"],
    ]
    columns_defensa: List[str] = ["Name", "Bloqueos", "Robos de balón", "Faltas en ataque", "Paradas", "Porcentaje de Paradas"]
    

    def give_team(self):

        self.datas = {}
        i = 0
        for data in self.data_ataque:
            print(self.data_ataque[i][4])
            self.datas[i] = [self.data_ataque[i][0], self.data_ataque[i][1], self.data_ataque[i][2], self.data_ataque[i][3], self.data_ataque[i][4], self.data_ataque[i][5]]
            #, self.data_ataque[i][1], self.data_ataque[i][2], self.data_ataque[i][3], self.data_ataque[i][4], self.data_ataque[i][5]
            porcen = (int(data[3]) / int(data[2])) * 100 
            self.data_ataque[i][4] = str(round(porcen)) + "%"
            # print(self.data_ataque[i])
            i += 1

        print(self.datas)

    def increment(self, item, resource):
        print(type(item))
        print(str(self.datas[int(item)][2]) + " mas uno")
        self.datas[int(item)][resource] = str(int(self.datas[int(item)][resource]) + 1)
    
    def decrement(self, item, resource):
        print(type(item))
        print(str(item))
        # print(str(self.datas[int(item)][2]) + " menos uno")
        print("Abajo es el resource")
        print(self.datas[int(item)][resource] + " Holaaaa")
        self.datas[int(item)][resource] = str(int(self.datas[int(item)][resource]) - 1) 


