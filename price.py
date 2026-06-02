#Compara-se os preços de um produto em diferentes estabelecimentos e aconselha o melhor local de compra para o usuário.

from time import sleep
p1 = float(input('Qual o preço da Margarina 500g no Atacadão?R$:'))
p2 = float(input('Qual o preço da Margarina 500g no Assai?R$'))
p3 = float(input('Qual o preço da Margarina 500g no Carrefour?R$'))
print('...Onde eu devo comprar?...')
sleep(2)
if p2 > p1 < p3:
    print(f'O melhor lugar para comprar é no Atacadão por {p1}')
elif p1 > p2 < p3:
    print(f'O melhor lugar para comprar é no Assai por {p2}')
else:
    print(f'O melhor lugar para comprar é no Carrefour por {p3}')