#DICCIONARIOS
 

print("\n\n ========== IMPRIMIENDO VALORES ========= ")

spam = {'color': 'red', 'age': 42}

for vals in spam.values():
    print(vals)

print("\n\n ========== IMPRIMIENDO KEYS ========= ")

for kkys in spam.keys():
    print(kkys)

print("\n\n ========== IMPRIMIENDO ITEMS ========= ")

for itm in spam.items():
    print(itm)


print("\n\n ========== Obteniendo KEYS para LISTA ========= ")

print(spam.keys()) #Obtenemos una lista de keys!!!
print(list(spam.keys())) #Podemos convertir a lista ese resultado



print("\n\n ========== IMPRIMIENDO DE TODO!!! ========= ")

for k, v in spam.items():
    print("Key: "+ k +" Value: "+ str(v)) #+"Item:"+str(i))



print("\n\n ========== IMPRIMIENDO DE TODO!!! ========= ")












