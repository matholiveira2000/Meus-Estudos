from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 numeros...')
    for cont in range(0, 5):
        n = randint(0, 100)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os pares da lista {lista} temos a soma de {soma}')


numero = list()
sorteia(numero)
somapar(numero)

