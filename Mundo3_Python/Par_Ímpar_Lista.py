lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg not in 'SsNn':
        print('Erro de digitação!')
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')