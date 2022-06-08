maior = 0
menor = 0
for peso in range(1, 4):
    p = float(input('peso da pessoa {}? '.format(peso)))
    if peso == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = p
        if peso < menor:
            menor = p
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))
