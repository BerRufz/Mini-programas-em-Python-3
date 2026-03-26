num = [2, 5, 9, 1]
num[2] = 3 #Substitui o valor
num.append(7) #Adiciona o valor entre "()"
num.insert(0, 4) #Não aparece na posição 0 por causa do "sort"
num.sort() #Coloca em ordem
num.pop(3) #Remove o valor na posição entre "()"
num.remove(1) #Remove o valor entre "()"
print(num)
print(f'Essa lista tem {len(num)} elementos')
