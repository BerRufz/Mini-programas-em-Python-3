#SEM "while True:" e "sorted()"
lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[len(lista) - 1]: #vai dar "append()" se for o primeiro ou o maior que o último valor
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista): #Vai do 0 até a última posição, no caso, 5
            if num <= lista[posicao]: #Se o valor inserido foi maior ou igual, ele será adicionado da seguinte forma abaixo:
                lista.insert(posicao, num)
                break
            posicao += 1
print('-=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
