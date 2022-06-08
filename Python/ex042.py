print('--=' *20)
print('Analisador de triangulos')
print('--=' *20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um  triangulos')
    if r1 == r2 == r3:
        print('EQULATERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos não formam um triangulo')
