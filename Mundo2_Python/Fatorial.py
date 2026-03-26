num = int(input('Digite um número \npara calcular o seu FATORIAL: '))
print('Calculando {}!'.format(num))
f = 1
while num > 0:
    print('{}'.format(num), end = '')
    if num > 1:
        print(' X ', end = '')
    else:
        print(' = ', end = '')
    f *= num
    num -= 1
print('{}'.format(f))
