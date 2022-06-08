fut = ('Atletico-mg', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
       'Bragantino', 'Fluminense', 'America-mg', 'Atletico-go', 'Santos',
       'Ceará', 'Internacional', 'São Paulo', 'Athletico -PR', 'Cuiaba',
       'Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense')
print('-='*20)
print('lista do BRASILEIRÃO:', end=' ')
print(fut)
print('-='*20)
print('Os 5 primeiros', end=' ')
print(fut[0:6])
print('-='*20)
print('OS 4 ULTIMOS', end=' ')
print(fut[16:21])
print('-='*20)
print('TIMES EM ORDEM ALFABETICA', end=' ')
print(sorted(fut))
print('-='*20)
print(f'A CHAPECOENSE ESTA NA {len(fut[:21])} POSIÇÃO')
print('-='*20)
