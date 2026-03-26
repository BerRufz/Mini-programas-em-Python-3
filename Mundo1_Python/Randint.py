from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador "pensar"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 10')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar!
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você ganhou!')
else:
    print('GANHEI! Eu pensei no número {}, e não no {}!'.format(computador, jogador))
