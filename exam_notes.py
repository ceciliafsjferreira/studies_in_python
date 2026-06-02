#Simulador de resultado de aprovação/reprovação de notas:

aluno = dict()
aluno['Nome:'] = str(input('Qual o nome do aluno?'))
aluno['Média:'] = float(input('Qual a média do aluno?'))
if aluno['Média:'] >= 7:
    aluno['Situação'] = 'Aprovado.'
elif 6 <= aluno['Média:'] :
    aluno['Situação'] = 'De recuperação.'
else:
    aluno['Situação'] = 'Reprovado!'
for k, v in aluno.items():
    print(f'{k}: {v}')