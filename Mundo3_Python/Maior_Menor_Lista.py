val = []
maior = menor = 0
for n in range(0, 5):
    val.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = menor = val[n]
    else:
        if val[n] > maior:
            maior = val[n]
        if val[n] < menor:
            menor = val[n]
print(f'Você digitou os valores {val}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end = ' ')
for posicao, v in enumerate(val):
    if v == maior:
        print(f'{posicao}...', end = ' ')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end = ' ')
for posicao, v in enumerate(val):
    if v == menor:
        print(f'{posicao}...', end = ' ')
print()
