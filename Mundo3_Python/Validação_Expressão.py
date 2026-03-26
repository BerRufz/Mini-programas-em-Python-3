expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() #Ele remove o '(' da lista para que no fim, se for lista = 0, ela estará correta!
        else:#Se não tiver o '(', ele adiciona o ')', dessa forma, dando errado no final!
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está ERRADA!')
