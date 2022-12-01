#Funcion Print

def spam():
    global huevos
    huevos = "SPAM"


huevos = "ESTE ES GLOBAL"
print("Antes: "+huevos)
spam()
print("Despues:"+ huevos)