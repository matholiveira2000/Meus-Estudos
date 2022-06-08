from random import randint
from time import sleep
from operator import itemgetter
j = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
ranking = list()
for k, v in j.items():
    print(f'O {k} tirou o dado {v}')
    sleep(1)
print('-=' * 50)
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)
print('>>>>> RANKING DOS JOGADORES <<<<<<<')
for i, v in enumerate(ranking):
     print(f'{i+1} O {v[0]} ficou na  posição {v[1]}')
     sleep(1)
