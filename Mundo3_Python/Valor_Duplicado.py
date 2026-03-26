val = []
while True:
    num = int(input('Digite um valor: '))
    if num in val:
        print('Valor duplicado! Não será adicionado na lista! ')
    else:
        val.append(num)
        print('Valor adicionado com sucesso...')
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg in 'Nn':
        break
print('-=-' * 30)
print(f'Você digitou os valores {sorted(val)}')
