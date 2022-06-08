def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} é de {a}')


print('Controle de terrenos')
print('--' * 20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
