from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p += 1
    print('~~' * 30)
    print(f'Iniciando contagem de {i} ate {f} de  {p} em {p}')
    print('~~' * 30)
    sleep(2)
    if i < f:
        cont = i
        while cont < f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM')


contador(0, 200, 30)
print('Iniciando contagem personaliza...')
ini = int(input('INICIO:  '))
fim = int(input('FIM:     '))
passo = int(input('PASSO: '))
print('FIM')
contador(ini, fim, passo)