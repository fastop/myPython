#LISTAS AVANZADAS
import copy

#DEMO DE "ERROR" que se genera con listas en python!!!

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) #Comportamiento "raro", ya que se mete con la misma direccion al final del dia


#Para evitarlo usamos COPY / DEEPCOPY 

spam = ["A","B", "C", "D", "E"]
print(spam, id(spam))

queso = copy.copy(spam)
print(queso, id(queso))


queso[1] = 42 #Le movemos

print(spam)
print(queso)


#DEEPCOPY sirve para hacer lo mismo que COPY PERO... con listas que tienen listas dentro de la misma...
print("\n\n ========== DEEP COPY========= \n")

SS = [["A","B","C","D"],[1,2,3,4,["X","Y","Z"]]]
print(SS)

SSX = copy.copy(SS)
print(SSX)


SSY = copy.deepcopy(SS)
print(SSY)







