si = 0 #Soma das idades do grupo
mih = 0 #Maior idade homem
nomevelho = '' #Nome do homem mais velho
totmulhermenos20 = 0 #Total de mulheres com menos de 20 anos
for p in range(1, 5):
    print('---- {}a pessoa ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Gênero[M/F]: ')).strip()
    si += idade
    if p == 1 and gen in ('M', 'm'):
        mih = idade
        nomevelho = nome
    if gen in ('M', 'm') and idade > mih: #É a checagem após o primeiro laço, assim como no exercício anterior
        mih = idade
        nomevelho = nome
    if gen in ('F', 'f') and idade < 20:
        totmulhermenos20 += 1
media = si / 4
print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('Ao todo é(são) {} mulhere(s) com menos de 20 anos'.format(totmulhermenos20))
