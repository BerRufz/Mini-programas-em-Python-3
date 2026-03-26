num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: ')) #Fora e dentro, o "999" não será contabilizado 
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou o número {} vezes e a soma entre eles foi de {}'.format(cont, soma))
