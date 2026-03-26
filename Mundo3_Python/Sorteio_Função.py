from random import randint
from time import sleep

def sorteia(numeros):
    print('Sorteando os 5 valores da lista: ', end = ' ')
    for c in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        sleep(0.5)
        print(f'{n}', end = ' ')
    print('PRONTO!')

def somapar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma} ')

#Programa principal
numeros = []
sorteia(numeros)
somapar(numeros)
