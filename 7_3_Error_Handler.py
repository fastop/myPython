#Funcion Error Handler

def spam(numero):

    try:
        return 45/numero
    except ZeroDivisionError:
        print("ERROR: Argumento Invalido (como tú)")





print(spam(1))