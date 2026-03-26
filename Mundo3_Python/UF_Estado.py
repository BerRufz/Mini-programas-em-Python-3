#estado1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Aqui não pode-se usar o "[:]", pois irá para um dicionário
    #Aqui é criado um dicionário
print(brasil)
for e in brasil: #Cada dicionário em "brasil"
    for v in e.values():
        print(v, end = ' ')
    print()
    