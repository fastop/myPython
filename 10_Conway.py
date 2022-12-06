#CONWAY :: Juego de la vida
import random, time, copy

WIDTH = 60
HEIGHT = 20

#Creamos una lista para las celulas
nextCell = []

for x in range(WIDTH):
    column = [] #Creamos una nueva columna
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#") #Agregamos una celula viviente
        else:
            column.append(" ") #Agregamos una celula muerta
    nextCell.append(column) #nextCell es la lista de la lista de columnas
 

#El main LOOP
while True:
        print("\n\n\n\n\n") #Separamos cada paso con una nueva linea
        currentCells =  copy.deepcopy(nextCell)
        
        #Imprimimos currentCells en la pantalla
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end="") #Imprimimos el # o espacio
            print() #Imprimimos una nueva linea al final del renglon
        

        # Calculamos el siguiente paso de las celulas basados en el paso actual de celulas
        for x in range(WIDTH):
            for y in range(HEIGHT):
                #Obtenemos las coordenadas del vecino
                
                leftCoord =  (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT

                #Contamos el numero de vecinos con vida
                numNeighbors = 0

                if currentCells[leftCoord][aboveCoord] == "#":
                    numNeighbors += 1 #El vecino de arriba-izquierda esta vivo
                if currentCells[x][aboveCoord] == "#":
                    numNeighbors += 1 #El vecino de arriba esta vivo
                if currentCells[rightCoord][aboveCoord] == "#":
                    numNeighbors += 1 #El vecino de arriba-derecha esta vivo
                if currentCells[leftCoord][y] == "#":
                    numNeighbors += 1 #El vecino de la izquierda esta vivo
                if currentCells[rightCoord][y] == "#":
                    numNeighbors += 1 #El vecino de la derecha esta vivo
                if currentCells[leftCoord][belowCoord] == "#":
                    numNeighbors += 1 #El vecino de abajo-izquierda esta vivo
                if currentCells[x][belowCoord] == "#":
                    numNeighbors += 1 #El vecino de abajo esta vivo
                if currentCells[rightCoord][belowCoord] == "#":
                    numNeighbors += 1 #El vecino de abajo-derecha esta vivo

                # Colocamos la celula basados en las reglas del juego de la vida de Conway
                if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                    nextCell[x][y] == "#" #Celulas vivientes con 2 o 3 vecinos vivos
                elif currentCells[x][y] == " " and numNeighbors == 3: 
                    nextCell[x][y] = "#" #Celulas muertas con tres vecinos revive
                else:
                    nextCell[x][y] = " " # Todo lo demas muere o se queda muerto
                

        time.sleep(1) #Agregamos una pausa de un segundo para reducir el parpadeo

                
