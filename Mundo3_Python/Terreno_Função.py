def linhas(msg): #Cabeçalho
    print(msg)
    print('-=-' * len(msg))

def area(larg, comp): #Programa principal
    area = larg * comp
    print(f'A área de um terreno de {larg}m de largura e {comp}m de comprimento\n é igual a {area}m² ')

linhas('Controle de Terrenos') #Vai ler e ir lá para cima
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c) #Vai ler e ir lá para cima
