lista = []
dados = []
maisv = maisn = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Idade: ')))
    if len(dados) == 0:
        maisv = maisn = lista[1]
    else:
        if lista[1] > maisv:
            maisv = lista[1]
        if lista[1] < maisn:
            maisn = lista[1]
    dados.append(lista[:])
    lista.clear()
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while perg not in 'SsNn':
        print('Erro de digitação!')
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print(f'Ao todo foram cadastradas {len(dados)} pessoas')
print(f'A maior idade foi de {maisv} anos:', end = ' ')
for i in dados:
    if i[1] == maisv:
        print(f'{i[0]} ')
print(f'A menor idade foi de {maisn} anos:', end = ' ')
for i in dados:
    if i[1] == maisn:
        print(f'{i[0]} ')
