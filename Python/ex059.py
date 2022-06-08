from time import sleep
op = 0
soma = 0
multiplicar = 0
maior = 0
restaurar = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while op != 5:
    print('-=' * 20)
    op = int(input('''
 [ 1 ] SOMAR
 [ 2 ] MULTIPLICAR
 [ 3 ] MAIOR 
 [ 4 ] NOVOS NUMEROS 
 [ 5 ] SAIR DO PROGRAMA
 Sua opção: '''))
    print('-=' * 20)
    if op == 1:
        soma = v1 + v2
        print('A soma de {} e {} é {}'.format(v1, v2, soma))
    if op == 2:
        multiplicar = (v1 * v2)
        print('{} multiplicado por {} é igual {}'.format(v1, v2, multiplicar))
    if op == 3:
        if v1 > v2:
            maior = v1
        elif v2 > v1:
            maior = v2
            print('O maior numero entre {} e {} é {}'.format(v1, v2, maior))
    if op == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    if op == 5:
        print('Finalizando o programa')
        sleep(3)
    elif op > 5:
        print('valor invalido tente novamente')

