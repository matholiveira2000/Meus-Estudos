n = list()
impar = list()
par = list()
while True:
    n.append(int(input('Digite um numero: ')))
    f = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    if f == 'N':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os numeros digitados foram {n}')
print(f'Os numeros pares digitados foi {par}')
print(f'Os numeros impares digitados foi {impar}')
