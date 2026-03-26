from random import randint
computador = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(f'Os valores sorteados foram: {computador}')
print(f'O maior valor sorteado foi {max(computador)}')
print(f'O menor valor sorteado foi {min(computador)}')