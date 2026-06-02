#Geraçao de cadastro de pessoas leves e pesadas.

pessoas_leves = 0
pessoas_pesadas =0
pessoas_cadastradas = 0
dados = list()
while True:
    nomes = (str(input('Qual é o seu nome?:')))
    peso = (int(input('Qual é o seu peso?:')))
    pessoas_cadastradas += 1
    dados.append(nomes)
    dados.append(peso)
    if peso > 60:
       pessoas_pesadas += 1
    else:
       pessoas_leves += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
            break
print(f'O total de pessoas cadastradas foi de {pessoas_cadastradas}. Gerando a lista {dados}')
print(f'O total de pessoas leves foi de {pessoas_leves}, já de pessoas pesadas foi de {pessoas_pesadas}.')