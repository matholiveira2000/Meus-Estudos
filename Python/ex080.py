v = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in v:
       v.append(n)
    else:
        print('Valores duplicados')
    f = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if f == 'N':
        break
v.sort()
print(f'Os valores digitados foram {v}')

