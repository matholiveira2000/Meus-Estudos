
print('--=' *20)
print('Analisador de triangulos')
print('--=' *20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulos')
else:
    print('Os segmentos acima NÃO FORMA UM triangulo')