num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Unidade milhar: {}'.format(um))
print('Dezena milhar: {}'.format(dm))
print('Centena milhar: {}'.format(cm))