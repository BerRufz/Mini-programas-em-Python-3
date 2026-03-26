dal = int(input('Quantos dias o carro foi alugado? '))
qkm = float(input('Quantos km o carro andou? '))
pdia = dal * 60
pkm = qkm * 0.15
total = pdia + pkm
print('O preço a se pagar é {:.2f}'.format(total))