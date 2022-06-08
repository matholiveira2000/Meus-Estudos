d = dict()
l = list()
d['jogador'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {d["jogador"]} fez? '))
for c in range(0, tot):
    l.append(int(input(f'Quantos gols na partida {c + 1}? ')))
d['gols'] = l[:]
d['total'] = sum(d['gols'])
print('-='*50)
print(d)
print('-='*50)
for k, v in d.items():
    print(f'- O campo {k} tem o valor {v}')
print('-='*50)
print(f'O jogador {d["jogador"]} jogou {len(d["gols"])} partidas')
for i, v in enumerate(d['gols']):
    print(f'-> Na partida {i +1} fez {v} Gols')
print('-='*50)
print('>>>> SCOUT DO JOGADOR FINALIZADA <<<<<<<')
print('-='*50)
