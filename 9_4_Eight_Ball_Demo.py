#LISTAS AVANZADAS

import random

messages = ["Es seguro",
            "Esta decidido que no",
            "Claro, definitivamente",
            "Se ve brumoso, intentalo de nuevo",
            "Pregunta de nuevo mas tarde",
            "Concentrate y pregunta de nuevo",
            "Mi respuesta es NO",
            "El Panorama no pinta bien",
            "Muy dudoso!!!"
            ]


#StepByStep
randomNumber = random.randint(0, len(messages))
randomNumber -= 1 #Quitamos por el N

print(messages[randomNumber])


#print(messages[random.randint(0, len(messages) - 1)]) #One Liner



























