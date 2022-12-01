#Ciclos WHILE

spam = 0

while spam < 5:
    print("QUE PEDO MONDO")
    spam = spam + 1


#Segunda parte


while True:
    print("\nDame tu nombre perro:")
    name = input()
    
    if name == "Salir":
        break

    print("Gracias Perrin "+name)
 


#Tercera parte

while True:
    print("\nQuien eres?")
    name = input()
    
    if name != "Salir":
        continue

    print("Gracias Perrin")
    break
 