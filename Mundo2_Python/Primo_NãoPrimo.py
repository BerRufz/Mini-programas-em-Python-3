cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0 and num % 1 == 0:
        cont += 1
        print('\033[32m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    print('{} '.format(c), end = ' ')
if cont == 2:
    print('\n\033[mO número {} foi divisível {} vezes \nPor isso ele É PRIMO!'.format(num, cont))
else:
    print('\n\033[mO número {} foi divisível {} vezes \nPor isso ele NÃO É PRIMO!'.format(num, cont))

