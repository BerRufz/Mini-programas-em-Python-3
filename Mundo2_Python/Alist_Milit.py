from datetime import date
atual = date.today().year
gen = str(input('Qual seu gênero? ')).strip().upper()
if gen == 'MASCULINO':
    nasc = int(input('ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Você ainda tem {} ano(s) para se alistar! O ano do seu alistamento será em {}'.format(saldo, ano))
    elif idade > 18:
        saldo1 = idade - 18
        ano1 = atual - saldo1
        print('Você já deveria ter se alistado há {} ano(s)! O ano do seu alistamento foi em {}'.format(saldo1, ano1))
    print('Tenha um bom dia!')
else:
    print('Apenas pessoas do gênero masculino podem se alistar! ')