sal = float(input('Qual o salário do funcionário? '))
if sal > 1250:
    sal1 = sal + (10 * sal / 100)
    print('Quem antes recebia R${}, passará a receber R${}!'.format(sal, sal1))
if sal <= 1250:
    sal2 = sal + (15 * sal / 100)
    print('Quem antes recebia R${}, passará a receber R${}!'.format(sal, sal2))
