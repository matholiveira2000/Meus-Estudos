import math
an = float(input('Digite o valor desejado: '))
s = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an, s))
c = math.cos(math.radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an, c))
t = math.tan(math.radians(an))
print('O angulo de {} tem a tangente de {:.2f}'.format(an, t))

