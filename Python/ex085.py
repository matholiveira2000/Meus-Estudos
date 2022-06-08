p = list()
mid = list()
maior = menor = 0
while True:
    p.append(str(input('nome: ')))
    p.append(float(input('Peso: ')))
    if len(mid) == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
    mid.append(p[:])
    p.clear()
    c = str(input('Quer continuar? [S/N] ')).upper()[0]
    if c == 'N':
        break
print(f'O total de pessoas cadastradas foi de {len(mid)}')
print(f'O maior peso foi de {maior} Kg',)
for x in mid:
    if x[1] == maior:
        print(f'{x[0]}')
print(f'O menor peso cadastrado foi de {menor} Kg')
for z in mid:
    if z[1] == menor:
        print(f'{z[0]}')
print('FIM')
