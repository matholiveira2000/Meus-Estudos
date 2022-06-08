from time import sleep


def maior(*num):
    cont = m = 0
    print('\n Analisando os valores informados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {m}')


maior(1, 4, 20, 15)

