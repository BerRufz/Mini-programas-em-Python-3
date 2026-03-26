from random import randint
from time import sleep
import sys
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if 0 <= jogador <= 2:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print('-=-' * 10)
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('-=-' * 10)
    if computador == 0: #Computador PEDRA
        if jogador == 0:
            print('EMPATE')
        if jogador == 1:
            print('JOGADOR GANHOU')
        if jogador == 2:
            print('COMPUTADOR GANHOU')
    if computador == 1: #Computador PAPEL
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        if jogador == 1:
            print('EMPATE')
        if jogador == 2:
            print('JOGADOR GANHOU')
    if computador == 2: #Computador TESOURA
        if jogador == 0:
            print('JOGADOR GANHOU')
        if jogador == 1:
            print('COMPUTADOR GANHOU')
        if jogador == 2:
            print('EMPATE')
else:
    print('Você muito engraçadinho, ein?!')
    sys.exit('ENCERRANDO PROGRAMA!')