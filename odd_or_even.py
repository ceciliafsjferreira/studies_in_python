#Seu número é impar ou par?

numero = int(input('Me diga um numero quarquer:'))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é par')
else:
    print(f'O Número {numero} é impar')