perg = 'S'
cont = med = soma = maior = menor = 0
while perg == 'S' and perg != 'N':
    num = int(input('Digite um valor: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0] #[0] é para considerar só a primeira letra
med = soma / cont
print('Você digitou {} números e a média entre eles foi de {}'.format(cont, med))
print('O maior número é {}, e o menor, {}'.format(maior, menor))
