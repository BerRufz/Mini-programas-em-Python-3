dist = float(input('Diga a distância da viagem: '))
if (dist <= 200):
    preço1 = dist * 0.50
    print('O valor a ser pago na viagem é R${}'.format(preço1))
if (dist > 200):
    preço2 = dist * 0.45
    print('O valor a ser pago na viagem é R${}'.format(preço2))

