num = int(input('Digite um número o qual deseja ver a tabuada: '))
for c in range(1, 11):
    tab = num * c
    print('{} X {:2} = {}'.format(num, c, tab))