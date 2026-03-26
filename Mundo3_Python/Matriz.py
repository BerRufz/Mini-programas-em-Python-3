matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3): #"for" de alimentação
    for j in range(0,3):
        matriz [i][j] = int(input(f'Digite um valor para [{i}, {j}]: ')) #Aqui da certo os dois([i] e [j]) pois já está declarado lá em cima com os zeros
for i in range(0,3): #"for" de visualização
    for j in range(0, 3): #Mostra os 3 números na mesma linha
        print(f'[{matriz[i][j]}]', end = ' ')
    print() #E esse comando faz o programa ir para linha de baixo


matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Digite um valor para [{i}, {j}]: "))) #Aqui só pode colocar o "[i]" pois eu não declarei os 0's, só existindo as listas(linhas)
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end = ' ')
    print()
