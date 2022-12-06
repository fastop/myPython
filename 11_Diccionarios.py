#DICCIONARIOS


miGanso = {"size":"fat", "color":"gray", "disposition":"loud"}

print(miGanso)
print(miGanso["size"])

frase = "Mi ganso es de color "+miGanso["color"]+" y esta "+miGanso["size"]
print(frase+"\n\n")


#Los diccionarios pueden usar NUMEROS (enteros) com Keys!!!! AMAZING!!!
spam = {12345:"Combinacion mamalona", 42:"Die Antwoord"}
frase = spam[12345]+" >> "+spam[42]

print(frase)



print("\n\n ========== Diccionarios V. Listas ========= \n")

#Los diccionarios se pueden comparar tal cual, las listas no...
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)  #FALSE

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  #True


#Tratar de accesar a un elemento inexistente nos data un suculento error
# spam = {'name': 'Zophie', 'age': 7}
# spam['color']  #NO EXISTE... da ERROR!!!

















