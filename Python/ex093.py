j = {}
t = []
l = []
while True:
    j.clear()
    j['jogador'] = str(input('Qual é o nome do jogador? '))
    tot = int(input(f'Quantas partidas o {j["jogador"]} jogou ? '))
    for c in range(0, tot):
        l.append(int(input(f'      Quantos gols na partida {c + 1}? ')))
    j['gols'] = l[:]
    j['total'] = sum(l)
    t.append(j.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print('cod', end='')
for i in j.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(t):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(t):
        print(f'Erro! Não existe jogador com o codigo {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {t[busca]["jogador"]}:')
        for i, g in enumerate(t[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-'*30)
