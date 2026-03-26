def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [1, 2, 3]
dobra(valores)
print(valores)

def soma(*valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores}, temos {soma}')

soma(1, 4, 29)
soma(3, 8, 99)
