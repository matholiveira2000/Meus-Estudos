soma = 0
cont = 0
for c in range(0, 500):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')

