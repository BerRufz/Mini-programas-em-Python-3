def notas(*notas, sit = False):
    """
    notas(*num, sit = False)
    Função para analisar notas e situação de alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com informações sobre a situação da turma
    """
    resp = {}
    resp['Total'] = len(notas)
    resp['Maior'] = max(notas)
    resp['Menor'] = min(notas)
    resp['Média'] = sum(notas) / 2
    if sit == True:
        if resp['Média'] >= 7:
            resp['Situação'] = 'Boa'
        elif resp['Média'] >= 5:
            resp['Situação'] = 'Razoável'
        else:
            resp['Situação'] = 'Ruim'
    return resp

#Programa principal
resp = notas(5.5, 3.5, 9.5, sit = True)
print(resp)
#help(notas)
