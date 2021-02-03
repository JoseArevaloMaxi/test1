#solo de uso de ejemplo

import random
metros_por_kilometro = 1000
super_heroes = ["Thor","IronMan","Hulk","CapitanAmerica"]

def tirar_dado(num):
    return random.randint(1 , num)

t = tirar_dado(6)

class Mesa:
    def __init__(self, materiales, num_patas, acabado, metros):
        self.materiales = [materiales]
        self.num_patas = num_patas
        self.metros = metros
        self.acabado = acabado

    def quitar_acabado(self):
        self.acabado = False

    def info(self):
        print(f"Mesa: {self.materiales}\nAcabado: {self.acabado}\n")