print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
perg = 10
total = 0
while perg != 0:
    total += perg #Total começará valendo 10, porém ao fim do "while" ele receberá outro falor por conta da "perg"
    while cont <= total: #Após a pergunta, "total" terá um novo valor também, pois total = perg
        print(primeiro, end = ' -> ')
        primeiro += raz
        cont += 1
    print('PAUSA')
    perg = int(input('Quantos termos você quer mostrar a mais? ')) #Após inserir o número, "perg" será outro valor desse digitado
print('FIM')