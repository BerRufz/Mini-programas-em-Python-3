from Módulo3.lib.interface import *

def arquivoexiste(arq):
    try:
        a = open(arq, 'rt') #"rt" quer significa "read and text"
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(arq):
    try:
        a = open(arq, 'wt+') #"wt+" significa "write and text", e o "+" é o que faz a mágica!
        a.close()
    except:
        print('\033[0;31mHouve um erro ao criar o arquivo!\033[m')
    else:
        print(f'\033[0;32mAquivo {arq} criado com sucesso!\033[m')

def lerarquivo(arq):
    try:
        a = open(arq, 'rt')
        #Não fechar, pois quero abrir!
    except:
        print('\033[0;31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '') #Substitui o "\n" por ""(vazio)
            print(f'{dado[0]:<30}{dado[1]:>3} anos') #Nome/Idade #"30" e "3" é a quant de carac alinhados ao lado escolhido

    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at') #"at" significa "append text"
    except:
        print('\033[0;31mErro ao ler o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mHouve um erro na hora de escrever os dados!\033[m')
            a.close()
