v1 = soma = cont = 0
v1 = int(input('Digite um valor [999 para parar]: '))
while v1 != 999:
    soma += v1
    cont += 1
    v1 = int(input('Digite um valor [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles é {}'.format(cont, soma))




