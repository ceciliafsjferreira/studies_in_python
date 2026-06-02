#Tente adivinhar em qual número a máquina está pensando.

import random
import time
pc = random.randint(1, 10)
usuario = int(input('Em qual número você acha que eu pensei?'))
if usuario == pc:
    print('Processando...')
    time.sleep(3)
    print('Parabéns! Você adivinhou.')
else:
    print('Processando...')
    time.sleep(3)
    print('Puts...Você não conseguiu adivinhar')
    print(f'Esse foi o número em que pensei {pc}!')