#Correção de gabarito baseado nas respostas inseridas pelo usuário.

gabarito = {
    1:'D', 2:'A', 3:'C', 4:'B', 5:'A', 6:'D', 7:'C', 8:'C', 9:'A', 10:'B'
}
certas = []
erradas = []
nota = 0
for questao, acertos in gabarito.items():
     while True:
        resposta = str(input(f'Qual a resposta da questão {questao}(A, B, C ou D):')).upper()
        if resposta in ['A','B','C','D']:
           break
        print('Dado invalido')
     if resposta == gabarito[questao]:
        certas.append(questao)
        nota += 1
        print('Correto')
     else:
        print(f'Errado, a resposta é {gabarito[questao]}')
        erradas.append(questao)
print("-" * 30)
print(f'Você acertou {nota} questões.')
print(f'Respostas corretas: {certas}')
print(f'Respostas erradas: {erradas}')
