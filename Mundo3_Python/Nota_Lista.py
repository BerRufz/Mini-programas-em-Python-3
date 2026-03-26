listamin = []
#listageral = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listamin.append([nome, [nota1, nota2], media])
    #listageral.append(listamin[:]) #Neste exercício não será preciso
    #listamin.clear() #Neste exercício não será preciso
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while perg not in 'SN':
        print('Erro de digitação')
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-=-' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}') #<4 e <10 para alinhar à direita, e >8, à esquerda
print('-=-' * 30)
for indice, aluno in enumerate(listamin):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}') #"aluno" 0 e 2 são o nome e a média, respectivamente
while True:
    print('-=-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('ENCERRANDO PROGRAMA...')
        break
    if opc <= len(listamin) - 1: #"-1" por é de 0 ao valor, assim, contando o 0
        print(f'Notas de {listamin[opc][0]} são {listamin[opc][1]}')
print('VOLTE SEMPRE!')
