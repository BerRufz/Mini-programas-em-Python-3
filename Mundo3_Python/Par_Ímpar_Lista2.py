num = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}o valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 == 1:
        num[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')
