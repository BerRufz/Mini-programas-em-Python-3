import sys
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Encerrar programa''')
    opcao = int(input('>>>> Qual a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))
    if opcao == 2:
        print('O produto entre {} X {} é {}'.format(num1, num2, num1 * num2))
    if opcao == 3:
        if num1 > num2:
            print('O número {} é maior que {}'.format(num1, num2))
        if num1 < num2:
            print('O número {} é maior que {}'.format(num1, num2))
        if num1 == num2:
            print('Ambos são iguais')
    if opcao == 4:
        print('Informe os novos números!')
        num1 = int(input('Digite o número: '))
        num2 = int(input('Digite o outro número: '))
    if opcao == 5:
        sys.exit('Encerrando programa...')