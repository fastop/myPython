#LISTAS AVANZADAS
# ENUMS :: FOR NOT IN AND TRICKS de ASSIGNACION MULTIPLE !!!

print("\n ===== Buscando en Listas ==== \n")

myPets = ["Zophie", "Pooka", "Fat-Tail"]

print("Dame un nombre de mascota:")
name = input()

if name not in myPets:
    print("No hay ninguna mascota llamada "+ name)
else:
    print(name + " es mi mascota")

    

print("\n\n ========== Asignaciones Multiples (truco) ========= ")

cat = ["gordo", "gris", "ruidoso"]

print(cat)
cat, color, desc  = cat
print(cat, color, desc)



print("\n ==================== Usando ENUMS =================== ") #enumeration nos regresa DOS valores, el KEY y el valor

supplies = ["Plumas", "Engrapadoras", "Lanzallamas", "Carpetas"]

for index, item in enumerate(supplies):
    print("Index "+str(index)+ " la cosa es: "+item)




print("\n ==================== OPERADOR PARA AUMENTAR =================== ") 

spam = 42
spam = spam +1
print(spam)

spam += 1
print(spam)

bacon = ["Demo"]
bacon *= 3  #Multiplicamos la cantidad de elementos por tres
print(bacon)


print("\n ==================== Buscando el calor en la lista con INDEX() =================== ") 

spam = ["hello", "hi", "howdy", "heyas"]

print(spam.index("hello"))
print(spam.index("heyas"))

print(spam.index("xxx")) #Esto da ERROR!!!