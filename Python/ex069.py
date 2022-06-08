tot18 = totm20 = h = 0
while True:
    print('-' * 50)
    print('CADASTRE UMA PESSOA')
    print('-' * 50)
    id = int(input('IDADE: '))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('SEXO: [M/F] ')).strip().upper()[0]
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if id > 18:
        tot18 += 1
    if id < 20 and sx == 'F':
        totm20 += 1
    if sx == 'M':
        h += 1
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos ')
