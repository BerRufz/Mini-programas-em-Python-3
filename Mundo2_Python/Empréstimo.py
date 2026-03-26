vcasa = float(input('Valor da casa: R$'))
scomp = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = vcasa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(vcasa, anos))
print('a prestação será de R${:.2f}'.format(prest))
if prest <= (30 * scomp / 100):
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo NEGADO!')

