#IMPORTS
import random, sys

print("--------------------------------")
print("PIEDRA, PAPEL o TIJERAS")
print("--------------------------------")

#Estas variables serviran para llevar un registro de las ganadas y perdidas (y empates).
wins = 0
losses = 0 
ties = 0
rex = ""

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    while True:
        print("--------------------------------")
        print("\nSelecciona opcion")
        print(" [1] Piedra 💎 | [2] Papel 📃  | [3] Tijera ✂ | [0] Salir")
        playerMove = input()

        if playerMove == "0":
            sys.exit()
        if playerMove == "1" or playerMove == "2" or playerMove == "3":
            break  #Nos salimos del ciclo de seleccion

        print("Escribe 1,2,3 o 0")

    #Mostramos la eleccion del jugador

    if playerMove == "1":
        rex = "💎 PIEDRA contra"
    elif playerMove == "2":
        rex = "📃 PAPEL contra"
    elif playerMove == "3":
        rex = "✂ TIJERA contra"

    playerMove = int(playerMove) #Lo hacemos entero

    #Desplegamos lo que eligio la computadora

    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        rex = rex+" PIEDRA 💎"
    if randomNumber == 2:
         rex = rex+" PAPEL 📃"
    if randomNumber == 3:
         rex = rex+" TIJERA ✂"

    print(rex)

    #Mostramos los records de ganas y perdidas 
    if  playerMove == randomNumber:
        print("EMPATE 💢")
        ties = ties + 1
    elif playerMove == 1 and randomNumber == 3:
        print("GANASTE PERRI 🥇")
        wins = wins + 1
    elif playerMove == 2 and randomNumber == 1:
        print("GANASTE PERRI 🥇")
        wins = wins + 1
    elif playerMove == 3 and randomNumber == 2:
        print("GANASTE PERRI 🥇")
        wins = wins + 1
    else:
        print("PERDISTE PERRIN 👎")
        losses = losses + 1

