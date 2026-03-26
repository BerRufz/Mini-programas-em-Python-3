lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while perg not in 'SN':
        print('Erro de digitação!')
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-=-' * 30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valortes em ordem decrescente são {sorted(lista, reverse = True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
