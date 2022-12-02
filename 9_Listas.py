#LISTAS

#Lista sencilla

spam = ["perro", "gato", "murcielago","perra"]
print(spam[0]) #impresion normal de dato

spamix = ["perro", "gato", "murcielago","perra", 0, True] #datos mixtos, le vale

spammo = [["perro", "gato", "perra"], [11,22,33,44,55]]

print(spammo[0]) #print ["perro", "gato", "perra"]
print(spammo[0][1]) #print gato

#Tomando posiciones "negativas"
print(spam[-1]) #print perra
print(spam[-2]) #print muercielago

#armando slices
print(spam[0:4]) #Mostramos todo ['perro', 'gato', 'murcielago', 'perra']  
print(spam[1:3]) #Mostramos del 1 al 3 ['gato', 'murcielago']

print(spam[0:-1]) #Tambien se puede hacer con negativos ['perro', 'gato', 'murcielago']


#Tambien se puede acortar el rango de la siguiente manera   ['perro', 'gato']
print(spam[:2]) #Imprimimos hasta el segundo elemento       ['gato', 'murcielago', 'perra']
print(spam[1:]) #Imprimimos a partir del elemento 1 hasta el final  ['perro', 'gato', 'murcielago', 'perra']  
print(spam[:]) #Imprimimos TODOS


#Obtener la longitud de la lista
print(len(spam))


#Cambiando valores
print("===  Cambiando Valores ===\n")

print("Antes :", spam)
spam[1] = "PERRINES"
spam[-1] = "Cambiando el ultimo"
print("Despues :", spam)