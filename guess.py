#Adivinhe o número que o computador está pensando:

import random
import time
pc = random.randint(0, 10)
print('Sou o seu computador...Acabei de pensar em um número!')
print('Será que você consegue adivinhar?')
acertar = False
palpites = 0
while not acertar:
    usuario = int(input('Qual o seu palpite?\nR:'))
    palpites +=1
    if usuario == pc:
        acertar = True
    else:
        if usuario > pc:
            print('Processando...')
            time.sleep(2)
            print('Um pouco menos...')
        elif usuario > pc:
            time.sleep(2)
            print('Processando...')
            print('Um pouco mais...')
print('Processando...')
time.sleep(3)
print(f'Você acertou em {palpites} palpite(s). PARABÉNS!!!!!!')
