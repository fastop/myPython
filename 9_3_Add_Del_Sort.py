#LISTAS AVANZADAS
    # Agregar/Eliminar/Organizar


print("\n ==================== AGREGANDO VALORES CON APPEND =================== ") 

spam = ["cat", "dog", "bat"]
print (spam)
spam.append("Moose")
print (spam)



print("\n ==================== AGREGANDO VALORES CON INSERT =================== ") 
spam = ["cat", "dog", "bat"]

print(spam)
spam.insert(1, "Chicken")
print(spam)


print("\n ==================== ELIMINANDO VALORES CON REMOVE =================== ") 

spam = ["cat", "bat", "rat", "elephant"]
print(spam)
spam.remove("bat")
print(spam)


print("\n ==================== Si el elemento existe muchas veces ... =================== ") 
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print(spam)
spam.remove("cat"); #Solo elimina la primera ocurrencia 
print(spam)




print("\n ==================== ORDENAR VALORES EN UNA LISTA CON SORT() =================== ") 

spam = [2, 5, 3.14, 1, -7]
print(spam)
spam.sort()
print(spam)


print("\n ==================== ORDENAR VALORES EN UNA LISTA CON SORT() [STRING] =================== ") 

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort()
print(spam)


print("\n ==================== ORDENAR VALORES INVERSOS EN UNA LISTA CON SORT() =================== ") 

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort(reverse=True)
print(spam)

# SORT MIX
# spam = [1, 3, 2, 4, 'Alice', 'Bob'] #ESTO NO SIRVE PARA SORT
# spam.sort()


print("\n ==================== ASCCI ORDER SORT() =================== ") 
#SORT organiza por ASCII, no por letra por ello las mayusculas van primero que las minusculas

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
print(spam)
spam.sort()
print(spam)

#PERO, si quieres organizarlo awuebito... haz todo minusculas ...

spam = ['a', 'z', 'A', 'Z']
print(spam)
spam.sort(key=str.lower)
print(spam)


print("\n ==================== REVERSEANDO LOS VALORES EN UNA LISTA =================== ") 

spam = ['cat', 'dog', 'moose']
print(spam)
spam.reverse()
print(spam)

































