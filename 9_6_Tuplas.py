#LISTAS AVANZADAS
 
 #Las tuplas son como listas pero en lugar de corchetes usan parentesis
 # ademas son inmutables :V

eggs = ("Holo", 42, 0.5)

print(eggs)
print(eggs[0])
print(eggs[1:3])

print(len(eggs))


print(type(('hello',)))
print(type(('hello')))


print("\n ==================== CONVIRTIENDO LISTA() >a> TUPLA() =================== ") #enumeration nos regresa DOS valores, el KEY y el valor

lista = ["perro", "gato", 666]
tupla = ("perro", "gato", 666)

print(lista, tuple(lista))
print(tupla , list(tupla))

#Partiendo un string
print(list("HOLO PERRO"))
print(tuple("HOLO PERRO"))



print(id(lista))
print(id(tupla))










