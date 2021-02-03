#===== DUELO POKEMON =====
from utilidades_extra import tirar_dado

print("===== DUELO POKEMON ===== \n")

class Pokemon:
    def __init__(self, nombre, ataque, player):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100
        self.player = player


    def gano(self):
        print(f"Su Pokemon {self.nombre} ha quedado con {self.vida} puntos de vida\n")

#creamos nuestros Pokemones

a1 = Pokemon("Pikachu", 24,1)
a2 = Pokemon("Bulbasaur", 29,1)
a3 = Pokemon("Miau", 32,1)
a4 = Pokemon("Snorglax", 29,1)
a5 = Pokemon("Onix", 26,1)
a6 = Pokemon("Ponitash",28,1)
a7 = Pokemon("Mew Two", 30,1)

b1 = Pokemon("Pikachu", 24,2)
b2 = Pokemon("Bulbasaur", 29,2)
b3 = Pokemon("Miau", 32,2)
b4 = Pokemon("Snorglax", 29,2)
b5 = Pokemon("Onix", 26,2)
b6 = Pokemon("Ponitash",28,2)
b7 = Pokemon("Mew Two", 30,2)
while True:
    try:
        print("Elige tus Pokemones, escribe el numero correspondiente\n"
        "1 = Pikachu\n"
        "2 = Bulbasaur\n"
        "3 = Miau\n"
        "4 = Snorglaxa\n"
        "5 = Onix\n"
        "6 = Ponitash\n"
        "7 = Mew Two\n")

        player1 = input("Player1: >")
        if player1 == "1":
            player1 = a1
        elif player1 == "2":
            player1 = a2
        elif player1 == "3":
            player1 = a3
        elif player1 == "4":
            player1 = a4
        elif player1 == "5":
            player1 = a5
        elif player1 == "6":
            player1 = a6
        elif player1 == "7":
            player1 = a7
        else:
            print("escribiste mal el num del Pokemon")
        print(player1.nombre)

        player2 = input("Player 2: >")
        if player2 == "1":
            player2 = b1
        elif player2 == "2":
            player2 = b2
        elif player2 == "3":
            player2 = b3
        elif player2 == "4":
            player2 = b4
        elif player2 == "5":
            player2 = b5
        elif player2 == "6":
            player2 = b6
        elif player2 == "7":
            player2 = b7
        else:
            print("escribiste mal el num del Pokemon")
        print(player2.nombre,"\n")

    #iniCializamos los valores
        a1.vida = 100
        a2.vida = 100
        a3.vida = 100
        a4.vida = 100
        a5.vida = 100
        a6.vida = 100
        a7.vida = 100
        b1.vida = 100
        b2.vida = 100
        b3.vida = 100
        b4.vida = 100
        b5.vida = 100
        b6.vida = 100
        b7.vida = 100

        turno = tirar_dado(2)

        print(f"{player1.nombre} se enfrenta a {player2.nombre}\n")
        print("====== ¡COMIENZA LA BATALLA! =======\n")

        while player1.vida > 0 and player2.vida > 0:
            if turno == 1:
                player2.vida = player2.vida - player1.ataque
                turno = 2
                print(f"El {player1.nombre} de player{player1.player} ataca y le quita {player1.ataque} puntos de vida a {player2.nombre} de player {player2.player}")
                print(f"{player2.nombre} de player{player2.player} queda con {player2.vida} puntos de vida\n")
            else:
                player1.vida = player1.vida - player2.ataque
                turno = 1
                print(f"El {player2.nombre} de player{player2.player} ataca y le quita {player2.ataque} puntos de vida a {player1.nombre} de player {player1.player}")
                print(f"{player1.nombre} de player{player1.player} queda con {player1.vida} puntos de vida\n")

        if player1.vida <= 0:
            print("Player2 ha ganado")
            player2.gano()

        else:
            print("Player1 ha ganado")
            player1.gano()
    except AttributeError as err:
        print(err)

    volver = input("Quieres volver a intentarlo? escribe (s) para aceptar, sino escribe cualquier otro caracter\n> ")
    if volver != "s":
        break

print("\nBye, orina antes de dormir :P ")

