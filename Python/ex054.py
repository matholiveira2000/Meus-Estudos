maior = 0
menor = 0
atual = 2022
for c in range(1, 8):
    n = int(input('Em que ano a {:2} pessoa nasceu? '.format(c)))
    idade = atual - n
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tivemos {} pessoas maior de idade'.format(maior))
print('E tivemos {} pessoas menor de idade'.format(menor))



