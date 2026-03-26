from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    sleep(2)
    if passo < 0: #Caso passo seja negativo
        passo *= -1
    if passo == 0: #Caso passo seja iguala a 0
        passo = 1
    if inicio < fim: #Contagem progressiva
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end = ' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    elif inicio > fim: #Contagem regressiva
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem! ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
