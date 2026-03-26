peso = float(input('Gigite seu peso: '))
h = float(input('Digite sua altura: '))
imc = peso / (h * h)
if imc < 18.5:
    print('Com o imc de {:.2f}, você está ABAIXO DO PESO!'.format(imc))
if 18.5 < imc < 25:
    print('Com o imc de {:.2f}, você está no PESO IDEAL!'.format(imc))
if 25 < imc < 30:
    print('Com o imc de {:.2f}, você está no SOBREPESO!'.format(imc))
if 30 < imc < 40:
    print('Com o imc de {:.2f}, você está na OBESIDADE!'.format(imc))
if imc > 40:
    print('Com o imc de {:.2f}, você está na OBESIDADE MÓRBIDA!'.format(imc))
print('Lembre-se: sua saúde é o seu maior bem!')
