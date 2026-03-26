print('-' * 30)
frase = 'CADASTRE UMA PESSOA'
print(f'{frase:^30}')
print('-' * 30)
tot18 = man = totm20 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        tot18 += 1
    print('-' * 30)
    gen = ' '
    while gen not in ('MF'):
        gen = str(input('Gênero [M/F]: ')).strip().upper()[0]
        if gen == 'M':
            man += 1
        if gen == 'F' and idade < 20:
            totm20 += 1
        print('-' * 30)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if perg == 'N':
        break
print(f'O total de pessoas com mais de 18 anos foi {tot18}')
print(f'O total de homens é de {man}')
print(f'O total de mulheres com menos de 20 anos é de {totm20}')
print('FIM!')

