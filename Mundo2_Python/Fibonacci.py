import sys
print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
terms = int(input('Quantos termos deseja mostrar? '))
if terms == 0:
    print('Você é muito engraçadinho, ein?!')
    sys.exit('Encerrando programa...')
t1 = 0
t2 = 1 #Esses dois números(t1 = 0 e t2 = 1) serão a base para o que virá no "while"
print('{} -> {}'.format(t1, t2), end = '')
cont = 2 #2, pois se for 1, será mostrado 1, 2, será mostrado 2 e a partir de 3 será o "while" abaixo
while cont <= terms:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM ')