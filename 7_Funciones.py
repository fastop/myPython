#Funciones

#Funcion normal
def holo():
    print("Que once con el doce")
    print("Asi son las basess papulince")


#Con parametros
def holox(nombre):
    print("Hola "+ nombre)


#Funcion con return!!!
def holoy(nombre):
    tmp = "Hola "+ nombre +"\n Bienvenido"
    return tmp


print("--------------------")
holo()
holo()
holo()

print("--------------------")
holox("Perrin")
holox("Perron")


print("--------------------")
print(holoy("Perrin"))
print(holoy("Perron"))

