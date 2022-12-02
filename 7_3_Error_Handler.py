#Funcion Error Handler

def spam(numero):

    try:
        return 45/numero
    except ZeroDivisionError:
        print("ERROR: Argumento Invalido (como tú)")



print(spam(1))



#Segunda Forma


def spamx(divideBy):
    return 42 / divideBy

try:
    print(spamx(2))
    print(spamx(12))
    print(spamx(0))
    print(spamx(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')