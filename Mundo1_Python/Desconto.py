price = float(input('Qual o preço do produto? R$'))
desc = price - price*5/100
print('O produto custa {:.2f}R$, na promoção de 5% o produto custará {:.2f}R$'.format(price, desc))