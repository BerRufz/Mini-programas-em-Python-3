lp = float(input('Qual a largura da parede? '))
ap = float(input('Qual a altura da parede? '))
area = lp * ap
tinta = area / 2
print('Sua parede tem dimensão {}x{} e sua área é de {}'.format(lp, ap, area))
print('Para pintar sua parede, é ncessário {}L de tinta'.format(tinta))

