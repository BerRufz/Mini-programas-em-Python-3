print('-=-' * 15)
print('10 termos de uma PA')
print('-=-' * 15)
num = int(input('Digite um número: '))
raz = int(input('Digite uma razão: '))
dec = num + (10-1) * raz
for c in range(num, dec + 1, raz):
    print(c, end = ' -> ')
print('\nACABOU')
