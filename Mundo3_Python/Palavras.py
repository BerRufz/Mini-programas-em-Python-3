palavras = ('aprender', 'parágrafo', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'grupo', 'saúde', 'mercado', 'grupo', 'programador',)
for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aáàâãeéêiíoóõôuú':
            print(letra.upper(), end = ' ')
