#O código abaixo compara os valores da tabela fip de um veículo em 3 anos diferentes.

a2023 = float(input('Qual o valor médio do carro do modelo Classic LS 1.0 de 2013 no ano de 2023:'))
#28
a2024 = float(input('Qual o valor médio do carro do modelo Classic LS 1.0 de 2013 no ano de 2024:'))
#26
a2025 = float(input('Qual o valor médio do carro do modelo Classic LS 1.0 de 2013 no ano de 2023:'))
if  a2023 > a2024 and a2023 > a2025:
    print(f'O maior valor foi {a2023}')
elif a2024 > a2023 and a2024 > a2025:
    print(f'O maior valor foi {a2024}')
else :
    print(f'O maior valor foi {a2025}')

if a2023 < a2024 and a2023 < a2025:
   print(f'O menor valor foi {a2023}')
elif a2024 < a2023 and a2024 < a2025:
   print(f'O menor valor foi {a2024}')
else:
    print(f'O menor valor foi {a2025}')