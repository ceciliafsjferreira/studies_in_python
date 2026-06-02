#O programa analisa o percentual de crescimento/queda de uma determinada empresa:

print('Gostaria de saber o percentual de crescimento da minha empresa.')
p_n = int(input('Me diga qual foi o faturamento mais antigo:'))
p_f = int(input('Me diga qual foi o faturamento mais recente:'))
percentual = (p_f - p_n)/p_n*100
if percentual > 0:
    if percentual > 50:
        print(f'O percentual foi positivo, tendo um crecimento de {percentual:.2f}%')
    else:
        print('Houve um crecimento de {percentual:.2f}%.É positivo.')
elif percentual < 0:
    print(f'Uma queda de {percentual:.2f}%. Melhore. ')
else:
    print(f'O crecimento foi de {percentual:.2f}%. ')