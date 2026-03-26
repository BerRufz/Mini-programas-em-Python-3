i = int(input('Digite um número: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
s = 0 
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório foi de {}'.format(s))