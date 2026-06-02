#Confira se você foi multado por alta velocidade, se sim, veja qual o valor do prejuizo.

velocidade = int(input('Qual a velocidade percorrida com o veiculo?'))
if velocidade <=80:
    print('Você está nos limites de velocidade')
else:
    print('Você foi multado.')
    print(f'A sua multa foi de R${(velocidade-80)*7}.')