#LISTAS AVANZADAS

spam = ["perro", "gato", "murcielago","perra"]
print(spam[0]) #impresion normal de dato

A = [1,2,3]
B = ["A","B","C"]

print("\n ===== CONCATENANDO ==== ")

print( A + B ) #Concatenando
print( A + ['AA','BB','CC']) #Concatenando a lo porko


print("\n ===== Eliminando Valores ==== ")

print(spam)
del spam[2] #Eliminamos "Murcielago"
print(spam)


print("\n ===== Agregamos Valores a las listas ==== ")

catNames = [] #Inicializamos la lista

while True:
    print("\nColoca el nombre de tu gato numero ["+str(len(catNames)+1)+ "]")
    name = input()

    if name == '': #Con enter salimos de aqui
        break

    catNames = catNames + [name] #Concatenamos a la lista

    print("El nombre de los gatos son: ")

    for name in catNames:
        print(" >>"+name)


