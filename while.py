#Neste código todos os números digitados pelo usuário são somados até que o mesmo interrompa.
resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
                menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
if quant > 0:
        media = soma/quant
print(f'A soma do total dos número foi de {soma} e a média foi de {media}')
print(f'O maior valor foi de {maior} e o menor foi de {menor}')
