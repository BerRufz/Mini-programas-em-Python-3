import sys
futebol = {} #Itens presentes aqui: Jogador, Gols, Totgols
partidas = [] #Quantidade de gols

futebol['Jogador'] = str(input('Nome do jogador: '))
totpart = int(input(f'Quantas partidas {futebol['Jogador']} jogou? '))
if totpart == 0:
    print('Jogador morto do krai KKKKKK')
    sys.exit('Tchau, brigado!')
if totpart > 0:
    for c in range(1, totpart +1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
futebol['Gols'] = partidas[:] #É a cópia da lista, pois nela foi add a quantidade de gols
futebol['Totgols'] = sum(partidas) #"sum" faz a somatória dos valores da lista "partidas

print('=-' * 30)
print(futebol)

print('-=-' * 30)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 30)
print(f'O jogador {futebol['Jogador']} jogou {totpart} partidas')

print('-=-' * 30)
for i, v in enumerate(futebol['Gols']): #É a cópia da lista(partidas)
    print(f'=> Na partida {i + 1}, fez {v} gols!')
print(f'Foi um total de {futebol['Totgols']} gols!')
