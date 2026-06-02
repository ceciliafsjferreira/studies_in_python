#Foi criado um código para retornar a soma de todos os números impares entre 1 e 500.
s = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print(f'A soma dos números impares multiplos de 3 entre 1 a 500 é {s}')

#Gemini
sum = sum(range(3, 501, 6 ))
print(sum)
