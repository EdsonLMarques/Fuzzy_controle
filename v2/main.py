#simple fuzzy that defines how much something is
import random

from fuzzy import Simple_Fuzzy
from random import *

saida = []
fuzzy = Simple_Fuzzy()
for i in range(-10,11):
    x = randrange(-10, 9) + randrange(0, 10)/10 + randrange(0, 10)/100
    print(f'''valor = {x}''')
    saida.append(fuzzy.calcula_fuzzy(x))
print(saida)