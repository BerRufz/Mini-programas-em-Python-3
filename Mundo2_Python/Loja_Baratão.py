print('-' * 30)
frase = 'LOJA SUPER BARATÃO'
print(f'{frase:^30}')
print('-' * 30)
totcompra = prod1000 = menor = cont = 0
barato = ''
while True:
    name = str(input('Nome do produto: '))
    prc = int(input('Preço: R$'))
    cont += 1
    totcompra += prc
    if prc > 1000:
        prod1000 += 1
    if cont == 1 or prc < menor:
        menor = prc
        barato = name
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print(f'O preço total da compra foi de R$ {totcompra:.2f}')
print(f'Temo(s) {prod1000} produto(s) que custa(m) mais de R$1000')
print(f'O produto mais barato foi o(a) {barato}, e custa R${menor}')
