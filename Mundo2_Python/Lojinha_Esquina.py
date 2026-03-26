print('-=-' * 10)
print('Lojinha da esquina')
print('-=-' * 10)
prec = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO: ')
print('[1] À vista em dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opção = int(input('Qual será a forma de pagamento? '))
if opção == 1:
    prec1 = prec - (prec * 10/100)
    print('Sua compra de R${} vai custar R${:.2f} no final'.format(prec, prec1))
if opção == 2:
    prec2 = prec - (prec * 5/100)
    print('Sua compra de R${} vai custar R${:.2f} no final'.format(prec, prec2))
if opção == 3:
    print('Sua compra vai custar R${:.2f} no final'.format(prec))
if opção == 4:
    parc = int(input('Quantas parcelas? x'))
    prec3 = (prec + (prec * 20/100)) / parc
    precfinal = prec + (prec * 20/100)
    print('Sua compra será parcelada em {} de R${} com juros'.format(parc, prec3))
    print('Sua compra de R${} vai custar R${:.2f} no final'.format(prec, precfinal))
else:
    print('Opção inválida!')
print('Obrigado pela preferência, tenha um bom dia!')

