#LISTAS AVANZADAS

print("\n ===== Buscando en Listas ==== \n")

myPets = ["Zophie", "Pooka", "Fat-Tail"]

print("Dame un nombre de mascota:")
name = input()

if name not in myPets:
    print("No hay ninguna mascota llamada "+ name)
else:
    print(name + " es mi mascota")

    

print("\n ===== Asignaciones Multiples (truco) ==== ")

cat = ["gordo", "gris", "ruidoso"]

print(cat)
cat, color, desc  = cat
print(cat, color, desc)



print("\n ===== Usando ENUMS ==== ") #enumeration nos regresa DOS valores, el KEY y el valor

supplies = ["Plumas", "Engrapadoras", ]
