listagem = ('lapis', 2.75,
            'Mochila', 55.80,
            'Estojo', 25.80,
            'Transferidor', 5.50,
            'Compasso', 9.99,
            'Canetas', 2.00,)
print('-'*40)
print(f'{" LISTAGEM DE PREÇOS ":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' *30)
