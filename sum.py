def area(l, h):
    a = l * h
    print(f'A área de um terreno {l}x{h} = {a}')
def lin():
    print('-' * 30)


lin()
largura = float(input('Qual a largura do terreno:'))
altura = float(input('Qual a altura do terreno:'))
lin()
area(largura, altura)


