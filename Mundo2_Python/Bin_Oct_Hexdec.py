num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if (opção == 1):
    print('{} convertido em binário é {}'.format(num, bin(num) [2:] ))
elif (opção == 2):
    print('{} convertido em octal é {}'.format(num, oct(num) [2:] ))
elif (opção == 3):
    print('{} convertido em hexadecimal é {}'.format(num, hex(num) [2:] ))
else:
    print('Opção inválida! Tente novamente. ')