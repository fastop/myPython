#LISTAS AVANZADAS
 

nombre ="Perrin Perruno"

#Esto daria error ya que los strings son inmutables (no se pueden modificar)
# nombre[3] = "r"

nuevoNombre = nombre[:6]+ " >> "+nombre[-3:]
print(nuevoNombre)


eggs = [1, 2, 3]
eggs = [4, 5, 6]

print(eggs)


del eggs[2]
print(eggs)
eggs.append(666)
print(eggs)




















