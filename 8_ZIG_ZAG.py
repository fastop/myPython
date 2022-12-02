#Armamos un ZIG ZAG !!!

import time,sys

indent = 0 #Cuantos espacios para identar
indentIcreasing = True # Para cuando crezca o no crezca la ideantacion

try:
    while True:        
        print(' ' * indent, end='')
        print("********")
        time.sleep(0.1) #Pausamos por 1/10 segundos

        if indentIcreasing:
            #incrementamos el numero de espacios
            indent = indent + 1

            if indent == 20: #Cambiamos la direccion 
                indentIcreasing = False
            
        else:
            indent =  indent - 1 #Decrementams el numero de espacios

            if indent == 0:
                indentIcreasing = True #Cambiamos la direccion

except KeyboardInterrupt:
    sys.exit()
 