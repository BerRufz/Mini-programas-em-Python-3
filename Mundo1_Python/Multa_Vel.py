vel = float(input('Qual a sua velocidade? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! O limite é de 80Km/h, então sua multa é de R${:.2f}!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
