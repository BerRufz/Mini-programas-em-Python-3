from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}a pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        cont += 1
    else:
        cont1 += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('E também tivemos {} pessoas menores de idade'.format(cont1))