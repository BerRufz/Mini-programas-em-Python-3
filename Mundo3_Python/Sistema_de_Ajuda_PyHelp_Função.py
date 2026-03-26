from time import sleep
c = ('\033[m',  #0 -> Sem cores
     '\033[0;30;41m',  #1 -> Fundo vermelho
     '\033[0;30;42m',  #2 -> Fundo Verde
     '\033[0;30;43m',  #3 -> Fundo amarelo
     '\033[0;30;44m',  #4 -> Fundo azul
     '\033[0;30;45m',  #5 -> Fundo roxo
     '\033[7;37m')  #6 -> Cinza

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4) #"\'\'" para escapar
    print(c[6], end = '')
    help(comando)
    print(c[0], end = '')
    sleep(2)

def titulo(msg, cor = 0):
    tamanho = len(msg) + 4 #Esse "+4" é apenas para estética
    print(c[cor], end = '')
    print('~' * tamanho)
    print(f'  {msg}') #Essa formatação com espaço é apenas para estética
    print('~' * tamanho)
    print(c[0], end = '') #Para "limpar" a cor que estava
    sleep(1)

#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
