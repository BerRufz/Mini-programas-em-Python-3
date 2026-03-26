lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#Tuplas são imutáveis
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-2:])

#for comida in lanche:
    #print(f'Eu vou comer {comida}')
#print('Comi pra caramba!')

#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]}')
#print('Comi pra caramba!')

#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')

#print(sorted(lanche)) #Coloca em ordem
#print(lanche)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(2)) #Conta quantas vezes aparece
print(c.index(2)) #Mostra a primeira posição em que aparece     