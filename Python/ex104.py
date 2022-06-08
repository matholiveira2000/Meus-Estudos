def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = input(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


numero = leiaInt('digite um numero: ')
print(f'Você acabou de digitar o numero {numero}')
