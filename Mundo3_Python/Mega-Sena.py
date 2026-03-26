from time import sleep
from random import randint
lista = []
jogos = [] #Essa lista conterá várias "lista"'s
print('-' * 30)
frase = 'JOGO DA MEGA SENA'
print(f'{frase:^30}')
print('-' * 30)
perg = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= perg:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1 #Contará a quantidade de números na lista sorteada
        if cont >= 6:
            break
    lista.sort() #Irá colocar a lista sorteada em ordem
    jogos.append(lista[:]) #Irá colocar essa lista sorteada em um conjunto maior de listas
    lista.clear() #Irá limpar o conteúdo da lista sorteada para que possa repetir o processo
    tot += 1 #Contará a quantidade de listas sorteadas concluídas(jogos)
print('-=-' * 5, f'SORTEANDO {perg} JOGOS', '-=-' * 5)
sleep(1)
for indice, listaaaa in enumerate(jogos): #"indice" seria a lista(0,1,2...) dentro de "jogos", e "listaaaa" seria o conteúdo dentro dessa lista
    print(f'Jogo {indice + 1}: {listaaaa}')
    sleep(1)
print('-=-' * 5, 'BOA SORTE!', '-=-' * 5)
