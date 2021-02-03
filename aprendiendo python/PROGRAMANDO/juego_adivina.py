#Adivina el nro 2.0 PARA CANTIDADES MAS GRANDES , si miras abao en comillas esta la version 1.0
# le agregue un bucle infinito con el si quiere jugar o no.




nombre = input("Hola como te llamas?: \n")

print("Ok "+ nombre +" estoy pensando un numero entre 1 y 100, adivina cual es!")
print("Ojo tienes solo 10 intentos")

juega = input("Para jugar escribe una (s) si no escribe cualquier otra letra \n")
import random
limite = 100
adivina = random.randint(1, limite)
intentos = 0

while juega == "s":
    while intentos < 10:
        num = int(input("El nro que usaras esta vez es: \n"))
        if num == adivina:
            print("GANASTE!")
            juega = input("Para jugar escribe una (s) si no escribe cualquier otra letra \n")
            if juega == "s":
                import random
                adivina = random.randint(1, limite)
                intentos = 0
                print("EMPECEMOS DE NUEVO")
            else:
                print("BYE")
                break
        else:
            intentos += 1
            if intentos == 10:
                print("Ya usaste tus 10 intentos, PERDISTE!")
                juega = input("Para jugar escribe una (s) si no escribe cualquier otra letra \n")
                if juega == "s":
                    import random
                    adivina = random.randint(1, limite)
                    intentos = 0
                    print("EMPECEMOS DE NUEVO")
                else:
                    print("BYE")
            elif num > adivina:
                print("Intenta con un numero mas bajo")
            else:
                print("Intenta con un numero mas alto")




"""
#ADIVINA EL NRO BASICO
import random

adivina = random.randint(1,20)

print("Hola como te llamas?")
nombre = input()

print("Ok "+ nombre +" estoy pensando un numero entre 1 y 20, adivina cual es!")
print("Ojo tienes solo 3 intentos")

print("El nro que usaras para tu primer intento es: ")
num = int(input())

if num == adivina:
    print("WOW GANASTE A lA PRIMERA!")
else:
    if num > adivina:
        print("Te fuiste, intenta con un numero mas pequeño")
    else:
        print("Trata con al algo mas alto")
    print("El nro que usaras para tu segundo intento es: ")
    num = int(input())
    if num == adivina:
            print("GANASTE!")
    else:
        if num > adivina:
            print("Te fuiste, intenta con un numero mas pequeño")
        else:
            print("Trata con al algo mas alto")
        print("El nro que usaras para tu ultimo intento es: ")
        num = int(input())
        if num == adivina:
                print("GANASTE!")
        else:
                print("PERDISTE :(")
"""


