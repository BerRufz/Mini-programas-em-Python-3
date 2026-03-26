from random import randint
print('-=-' * 30)
print('JOGO DO PAR OU ÍMPAR')
print('-=-' * 30)
vit = 0
while True:
    pc = randint(1, 100)
    num = int(input('Digite um número: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    if pi not in 'PI':
        print('Você é muito engraçadinho, ein?!')
    print('-' * 30)
    soma = num + pc
    if pi == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU!')
            print('Vamos jogar novamente...')
            print(f'Você digitou {num}, e o computador, {pc}. O total de {soma} é PAR')
            print('-' * 30)
            vit += 1
        else:
            print('VOCÊ PERDEU!')
            print(f'Você digitou {num}, e o computador, {pc}. O total de {soma} é ÍMPAR')
            print('-' * 30)
            break
    if pi == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU!')
            print('Vamos jogar novamente...')
            print(f'Você digitou {num}, e o computador, {pc}. O total de {soma} é ÍMPAR')
            print('-' * 30)
            vit += 1
        else:
            print('VOCÊ PERDEU!')
            print(f'Você digitou {num}, e o computador, {pc}. O total de {soma} é PAR')
            print('-' * 30)
            break
print(f'Ao todo foi(foram) {vit} vitória(s)')
