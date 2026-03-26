import math
ang = float(input('Digite o ângulo que deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o valor de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o valor de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem o valor de {:.2f}'.format(ang, tan))