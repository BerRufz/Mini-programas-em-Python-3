a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))
#Verificando quem é menor
menor = a
if b < a and b < c and b < d:
    menor = b
if c < a and c < b and c < d:
    menor = c
if d < a and d < b and d < c:
    menor = d
#Verificando quem é maior
maior = a
if b > a and b > c and b > d:
    maior = b
if c > a and c > b and c > d:
    maior = c
if d > a and d > b and d > c:
    maior = d
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
