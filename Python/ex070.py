soma = mil = menor = cont = 0
b = ' '
while True:
    np = str(input('Nome do Produto: ')).strip()
    p = float(input('Preço: R$'))
    soma += p
    cont += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 1:
        menor = p
        b = p
    else:
        if p < menor:
            menor = p
            b = p
    if p > 1000:
        mil += 1
    if c == 'N':
        break
print(f'O produto mais barato foi {np} comprado por R$ {menor:.2f}')
print(f'Temos {mil} produtos que custa mais R$1000.00')
print(f'O total de compras foi de R${soma}')
