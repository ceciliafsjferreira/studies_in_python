#Solicita-se 3 números ao usuário, retornando os três em ordem crescente.

numero_um = int(input('Me dê um número inteiro:'))
numero_dois = int(input('Me dê outro número inteiro:'))
numero_tres = int(input('Me dê um terceiro número inteiro:'))
if numero_um > numero_dois and numero_um > numero_tres and numero_dois > numero_tres:
    print(f'{numero_tres}, {numero_dois}, {numero_um}')
elif numero_dois > numero_um and numero_dois > numero_tres and numero_um > numero_tres :
    print(f'{numero_tres}, {numero_um}, {numero_dois}')
elif numero_tres > numero_um and numero_tres > numero_dois and numero_um > numero_dois :
    print(f'{numero_dois}, {numero_um}, {numero_tres }')
else:
    print(f'{numero_um}, {numero_dois}, {numero_tres }')