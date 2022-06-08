def ficha(n='<desconhecido>', gol=0):
   print(f'O jogador {n} fez {gol} gol(s) no campeonato')


jogador = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    ficha(gol=g)
else:
    ficha(jogador, g)
