num = [[], []]
valor = []
for c in range(1, 8):
    valor = int(input(f'Digite o valor {c}o : '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Os numeros pares digitados foi {num[0]}')
print(f'Os numeros impares digitados foi {num[1]}')
