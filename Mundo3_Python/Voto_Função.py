def voto(ano):
    from datetime import date #Dentro da função economiza memória!
    print('-' * 20)
    idade = date.today().year - ano
    if ano < 16:
        return f'Com {idade} anos: SEM IDADE PARA VOTAR!'
    if 16 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    if idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL!'

#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
