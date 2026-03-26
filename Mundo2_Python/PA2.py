print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão PA: '))
cont = 1
while cont <= 10:
    print(primeiro, end = ' -> ')
    primeiro += raz
    cont += 1
print('FIM')

