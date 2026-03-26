aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = int(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')