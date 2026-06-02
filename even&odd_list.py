# O programa pedirá números para o usuário e retornará uma lista de números ímpares e números pares.

numeros_pares = []
numeros_impares = []
totais = []
for i in range(1, 8):
    numero = int(input(f'Me dê um {i}° número:'))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
numeros_impares.sort()
numeros_pares.sort()
totais.append(numeros_pares[:])
totais.append(numeros_impares[:])
numeros_pares.clear()
numeros_impares.clear()
print(totais)