gen = str(input('Informe seu gênero: [M/F] ')).strip().upper()
while gen not in 'MF':
    gen = str(input('Dados inválidos. Por favor, informe seu gênero: ')).strip().upper()
print('Gênero {} registrado com sucesso!'.format(gen))