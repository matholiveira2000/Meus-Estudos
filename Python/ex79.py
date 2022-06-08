numero = []
maior  = 0
menor = 0
for c in range(0, 5):
    numero.append(int(input(f'Digite um numero para a posição {c}: ')))
    if c == 0:
        maior = menor = numero[c]
    else:
        if numero[c] > maior:
            numero[c] = maior
        if numero[c] < menor:
            menor = numero[c]

print(f'Os numeros digitados foi {numero}')
print(f'O maior valor é {maior} nas posições', end=' ')
for i, n in enumerate(numero):
    if n == maior:
        print(f'{i}....', end='')
print()
print(f'O menor valor é {menor} nas posições', end=' ')
for i, n in enumerate(numero):
    if n == menor:
        print(f'{i}.....', end='')
print()
