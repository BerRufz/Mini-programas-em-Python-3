nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
m = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, m))
if (m >= 7):
    print('O aluno está APROVADO!')
elif (m < 5):
    print('O aluno está REPROVADO!')
elif (5 < m < 7):
    print('O aluno está em RECUPERAÇÃO!')
print('Equipe de ensino, unidos por uma educação melhor!')