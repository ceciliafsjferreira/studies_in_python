#Digite um número de 1 a 9999 e o código retornará as unidades, dezendas, centenas e milhares.

num = int(input('Digite um numero inteiro de 1 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: {unidade}, Dezena: {dezena},Centena: {centena},Milhar: {milhar}')