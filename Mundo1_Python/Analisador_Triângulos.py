print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)
l1 = float(input('Insira um tamanho de segmento: '))
l2 = float(input('Insira um outro tamanho de segmento: '))
l3 = float(input('Insira um outro valor de segmento: '))
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('Com os segmentos {}, {} e {}, é possível formar um triângulo!'.format(l1, l2, l3))
else:
    print('Não é possível formar um triângulo!')