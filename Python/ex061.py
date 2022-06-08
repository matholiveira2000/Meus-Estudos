p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    r += p
    cont += 1
print('FIM')
