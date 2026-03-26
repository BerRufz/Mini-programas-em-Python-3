def leiaint(n):
    while True:
        try:
            n = int(input(n))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue #Retorna para o "while True"
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n



def leiafloat(n):
    while True:
        try:
            n = float(input(n))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n

