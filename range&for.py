#Fiz com que o código me retornasse todos os números pares entre 1 e 50.

from time import sleep
for c in range(1,51):
    pares = c % 2
    if pares == 0:
        sleep(1)
        print(c)