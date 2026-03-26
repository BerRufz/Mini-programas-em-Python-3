from lib.interface import * #"*" significa importar tudo
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)
    elif resp == 2:
        #opção de cadastrar uma pessoa!
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade) #Nome do arquivo/Nome/Idade
    elif resp == 3:
        #Opção de sair do sistema!
        cabecalho('\t\033[0;32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
