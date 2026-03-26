cont = ('zero', 'um', ' dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if perg in 'Nn':
            break
    print('Tente novamente.', end = ' ')

