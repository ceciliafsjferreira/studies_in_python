#Digite sua cidade e o programa retornará se há 'Santo' ou não em seu nome.

cidade = str(input('Qual o nome da cidade em que você mora? \n R: ')).strip().upper()
possui_ou_nao = cidade[:5] == 'SANTO'
print(f"A sua cidade tem como {possui_ou_nao} a presença do nome SANTO")