soma = cont = 0
while True:
    n = int(input('Digite um numero [E 999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'você digitou {cont} numeros, e a soma entre eles foi igual a {soma}')
