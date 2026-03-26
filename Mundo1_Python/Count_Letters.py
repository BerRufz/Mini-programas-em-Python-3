fr = str(input('Digite uma frase: ')).strip().upper()
print('A letra (A) apareceu {} vezes na frase',format(fr.count('A')))
print('A primeira letra (A) aparece na posição {} da frase'.format(fr.find('A')+1))
print('A última letra (A) aparece na posição {} da frase'.format(fr.rfind('A')+1))

