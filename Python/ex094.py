d = dict()
l = list()
soma = media = 0
while True:
    d['nome'] = str(input('Nome: ')).upper()
    while True:
        d['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if d['sexo'] in 'MF':
            break
        print('ERRO! digite apenas [M] ou [F]')
    d['idade'] = int(input('IDADE: '))
    soma += d['idade']
    l.append(d.copy())
    while True:
        c = str(input('Quer continuar? [S/N] ')).upper()[0]
        if c in 'SN':
            break
        print('ERRO! digite apenas [S] [N]')
    if c == 'N':
        break
print('*' * 30)
print(f'A) Ao todo foram cadastradas {len(l)} pesssoas')
media = soma / len(l)
print(f'B) A media de idade é de {media}')
print('C) as mulheres cadastradas foram,', end='')
for p in l:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}', end='')
print()
print('A lista de pessoas acima da media são', end='')
for p in l:
    if p['idade'] >= media:
        print('     ')
    for k, v in p.items():
        print(f'{k} = {v}', end='')
    print()
print('>>>>>>> FIM <<<<<<<<')

