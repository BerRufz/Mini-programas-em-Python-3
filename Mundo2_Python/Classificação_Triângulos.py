l1 = float(input('Digite o valor do primeiro segmento: '))
l2 = float(input('Digite o valor do segundo segmento: '))
l3 = float(input('Digite o valor do terceiro segmento: '))
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('É possível formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    if l1 != l2 != l3 and l1 != l3:
        print('ESCALENO!')
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('ISÓSCELES!')
else:
    print('Não é possível formar triãngulo!')

