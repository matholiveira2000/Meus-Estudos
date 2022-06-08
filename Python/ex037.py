from time import sleep
print('OLA SEJA BEM VINDO AO CONVERSOR DE BASES NUMERICAS')
sleep(2)
n = int(input('Digite um numero inteiro: '))
print('''Escolha um numero para conversão: 
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL     ''')
op = int(input('Sua opção: '))
if op == 1:
    print(' {} convertido para BINARIO é igual a {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
