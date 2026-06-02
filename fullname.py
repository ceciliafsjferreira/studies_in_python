#Digite o seu nome completo e o código retornará o número de letras totais, o número de letras do primeiro nome e suas versões com letras maiusculas e minusculas.

nome = str(input('Digite seu nome completo:')).strip()
print(f'Seu nome é {nome}')
print(f'Seu nome em letras maisculas é {nome.upper()}')
print(f'Seu nome em letras minusculas é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')