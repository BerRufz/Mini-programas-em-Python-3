num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)}')
else:
    print('O 9 não apareceu!')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1} posição')
else:
    print('O 3 não apareceu!')
print(f'Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
