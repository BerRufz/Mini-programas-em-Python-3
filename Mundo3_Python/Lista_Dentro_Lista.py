teste = list()
teste.append('Bernardo')
teste.append(19)
galera = list()
galera.append(teste[:]) #"[:]" faz uma cópia #Essa linha coloca o "antes"
teste[0] = 'Ber'
teste[1] = 10
galera.append(teste[:])#E essa junta o "antes" com o "depois"
print(galera)
galerinha = [['Bernardo', 19], ['Ber', 10], ['Nar', 49], ['Do', 54]]
for p in galerinha:
    print(f'{p[0]} tem {p[1]} anos de idade!')
    