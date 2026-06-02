#O código abaixo diferencia se a letra digitada pelo usuário é uma vogal ou uma consoante.

l = str(input('Digite uma letra:'))
if l in 'aAeEiIoOuU':
    print('É uma vogal')
else:
    print('É uma consoante')