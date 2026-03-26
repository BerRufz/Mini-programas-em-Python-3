def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número
    :param n: número inteiro
    :param show: "True" para mostrar a conta, e False, para não
    :return: o valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(f'{c}', end = ' ')
            if c > 1:
                print('x', end = ' ') #Sinal de vezes
            else:
                print('=', end = ' ') #Sinal de igual
        f *= c
    return f

#Programa principal
n = int(input('Deseja ver o fatorial de qual valor? '))
print(fatorial(n, show = True))
#help(fatorial)
