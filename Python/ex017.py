import math
co = float(input('qual o comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h1 = math.hypot(co, ca)
print('a hipotenusa é igual a {:.2f}'.format(h1))
