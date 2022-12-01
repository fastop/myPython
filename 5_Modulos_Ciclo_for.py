#IMPORT Ciclos FOR

import random

for i in range(5):
    print(random.randint(1,10))




rands = "";
for i in range(5):
    rands += rands + str(random.randint(1,10))+" - "

print(rands)
 