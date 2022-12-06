#DICCIONARIOS
 
birthdays = {"Memo": "Abril 1", "Bob":"Diciembre 12", "Carola": "Marzo 4"}

while True:
        print("\n\nDame un Nombre: (en blanco para salir): ")
        name = input()

        if name=="":
            break


        if name in birthdays:
            print(birthdays[name] +  " es el cumpleaños de "+ name)
        else:
            print("No cuento con la informacion de cumpleaño de "+ name)
            print("Cuando es su cumpleaños?")
            bday = input()

            birthdays[name] = bday
            print("La base de cumpleaños ha sido actualizada...")







