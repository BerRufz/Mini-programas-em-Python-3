from datetime import date

trab = {}
trab['Nome'] = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
trab['Idade'] = date.today().year - anonasc
trab['CLT'] = int(input('CLT: '))
if trab['CLT'] != 0:
    trab['Contratação'] = int(input('Ano de contratação: '))
    trab['Salário'] = int(input('Salário: '))
    trab['Aposentadoria'] = trab['Idade'] + (trab['Contratação']) + 35 - date.today().year
print('=-' * 30)
for k, v in trab.items():
    print(f'- {k} tem o valor {v}')
