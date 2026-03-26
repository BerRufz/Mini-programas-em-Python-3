def ficha(jog = '<Desconhecido>', gols = 0):
    print(f'O jogador {jog} fez {gols} gols!')

#Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: ')) #"g" é "str"
if g.isnumeric(): #Para verificar se é numérico
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g) #Se for digitado apenas o número de gols #Aqui chama a função
else:
    ficha(n, g) #Mostrará ambos #Aqui chama a função
