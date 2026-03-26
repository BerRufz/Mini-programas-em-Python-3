matriz = [[], [], []]
spar = mai = scol = 0
for i in range(0, 3): #"Abre" a linha para que seja digitado os números da coluna
    for j in range(0, 3): #Adiciona 3 números em coluna na linha "i"
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end = ' ')
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j] #Que são so valores digitados no primeiro "for"
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é {spar}')
for i in range(0, 3):
    scol += matriz[i][2] #Ele verá a sublista [i][2] dentro da lista "matriz"
print(f'A soma dos valores da terceira coluna é {scol}')
for j in range(0, 3):
    if j == 0:
        mai = matriz[1][j]
    elif matriz[1][j] > mai:
        mai = matriz[1][j]
print(f'O maoir valor da segunda linha é {mai}')
