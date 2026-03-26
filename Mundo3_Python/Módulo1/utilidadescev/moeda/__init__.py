def metade(prec=0, formato=False):
    """
    -> Para calcular metade do preço:
    :param prec: preço normal
    :param formato: para formatar em quantidade monetária
    :return: retorna a metade do preço
    """
    res = prec / 2
    return res if formato == False else moeda(res)


def dobro(prec=0, formato=False):
    """
    -> Para calcular o dobro do preço:
    :param prec: preço normal
    :param formato: para formatar em quantidade monetária
    :return: retorna o dobro do preço
    """
    res = prec * 2
    return res if formato == False else moeda(res)


def aumperc(prec = 0, taxa = 0, formato = False):
    """
    -> Para calcular o aumento de 10%:
    :param prec: preço normal
    :param formato: para formatar em quantidade monetária
    :return: retorna o aumento de 10% do preço
    """
    res = prec + (prec * taxa / 100)
    return res if formato == False else moeda(res)


def moeda(prec=0, moeda='R$'):
    return f'{moeda}{prec:.2f}'.replace('.', ',')


def resumo(prec=0, taxa = 10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(prec)}')  # "\t" é uma tabulação em coluna
    print(f'Metade do preço: \t{metade(prec, True)}')
    print(f'Dobro do preço: \t{dobro(prec, True)}')
    print(f'Com {taxa}% de aumento: \t{aumperc(prec, taxa,  True)}')
    print('-' * 30)

# help(metade)
# help(dobro)
# help(aumperc)
