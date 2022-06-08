v = list()
while True:
    v.append(int(input('Digite um valor: ')))
    f = str(input('Quer continuar: ')).strip().upper()[0]
    if f == 'N':
        break
print(f'Você digitou {len(v)} elementos')
v.sort(reverse=True)
print(f'Os valores em ordem decrescente ficou {v}')
if 5 in v:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')
