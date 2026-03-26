from datetime import date
anonasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - anonasc
if idade <= 9:
    print('Você tem {} anos!'.format(idade))
    print('Sua classificação é MIRIM!')
elif idade <= 14:
    print('Você tem {} anos!'.format(idade))
    print('Sua classificação é INFANTIL!')
elif idade <= 19:
    print('Você tem {} anos!'.format(idade))
    print('Sua classificação é JÚNIOR!')
elif idade <= 25:
    print('Você tem {} anos!'.format(idade))
    print('Sua classificação é SÊNIOR!')
elif idade > 25:
    print('Você tem {} anos!'.format(idade))
    print('Sua classificação é MASTER!')

