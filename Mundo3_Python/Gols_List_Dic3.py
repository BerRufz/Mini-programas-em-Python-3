import sys

futebol = {}
galera = []
time = []

soma = 0
while True:
    futebol.clear()
    futebol['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou? '))
    galera.clear()
    if partidas == 0:
        print('Jogador morto do krai KKKKKK')
        sys.exit('Tchau, brigado!')
    if partidas > 0:
        for c in range(1, partidas + 1):
            gols = int(input(f'Quantos gols na partida {c}? '))
            galera.append(gols)
        futebol['Gols'] = galera[:]
        futebol['Totgols'] = sum(galera)
        time.append(futebol.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    #while perg not in 'SN':
        #print('ERRO DE DIGITAÇÃO!')
        #perg = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 30) #A partir daqui, serão exibidos os dados
for i in futebol.keys():
    print(f'{i:<15}', end = ' ')
print()
print('-=-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}', end = ' ')
    for d in v.values():
        print(f'{str(d):<15}', end = ' ')
    print()
print('-=-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(futebol):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(futebol[busca]['Gols']):
            print(f'-> No jogo {i + 1} fez {g} gols')
    print('-=-' * 30)
print('FIM DO PROGRAMA!')
