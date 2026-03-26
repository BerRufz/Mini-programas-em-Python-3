print('-'*40)
print(f'{'Listagem de preços':^40}')
print('-'*40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 16,
            'Estojo', 26.40,
            'Transferidor', 9,
            'Compasso', 12.50,
            'Mochila', 49.50,
            'Canetas', 8,
            'Livros', 35.70,)
for posicao in range(len(listagem)):
    if posicao % 2 == 0: #O nome do produto está sempre em uma posição par
        print(f'{listagem[posicao]:.<30}', end = ' ')
    if posicao % 2 == 1:
        print(f'R${listagem[posicao]:>7.2f}')
        