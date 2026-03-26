dados = {}
galera = []
soma = media = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Gênero'] = str(input('Gênero [M/F]: ')).strip().upper()[0]
    while dados['Gênero'] not in 'MF':
        print('ERRO DE DIGITAÇÃO!')
        dados['Gênero'] = str(input('Gênero [M/F]: ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    galera.append(dados.copy())
    perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while perg not in 'SN':
        print('ERRO DE DIGITAÇÃO!')
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
media = soma / len(galera)
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas') #A)
print(f'A média de idade é {media:.2f} anos') #B)
print(f'As mulheres cadastradas foram ', end = ' ') #C)
for p in galera:
    if p['Gênero'] == 'F':
        print(f'[{p["Nome"]}]', end = ' ')
print()
print('Lista das pessoas que estão acima da média: ') #D)
for p in galera:
    if p['Idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end = ' ')
        print()
print('PROGRAMA ENCERRADO...')
