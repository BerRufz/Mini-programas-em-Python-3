from random import randint
cont = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar?')
computador = randint(0, 10)
palp = int(input('Qual o seu palpite? '))
cont += 1
while palp != computador:
    if palp < computador:
        palp = int(input('Mais... Tente mais uma vez! '))
        cont += 1
    if palp > computador:
        palp = int(input('Menos... Tente mais uma vez! '))
        cont += 1
    if palp == computador:
        print('PARABÉNS, VOCÊ ACERTOU!!!!')
        print('Você acertou com {} tentativas'.format(cont))

