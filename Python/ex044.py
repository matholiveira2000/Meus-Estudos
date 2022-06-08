produto = float(input('Digite o valor do produto: R$ '))
mdp = int(input('''Digite o metodo que você deseja pagar:
[ 1 ] À VISTA NO DINHEIRO / OU CHEQUE
[ 2 ] À VISTA NO CARTÃO 
[ 3 ] 2X NO CARTÃO 
[ 4 ] 3X OU MAIS NO CARTÃO
: '''))
if mdp ==1:
    print('O produto ficara a vista no valor de R$ {:.2f}'.format(produto - (produto * 10/100)))
elif mdp ==2:
    print('O produto ficara no valor de R$ {:.2f}'.format(produto - (produto * 5/100)))
elif mdp ==3:
    print('O produto ficara no valor de R$ {:.2f}'.format(produto))
elif mdp ==4:
    print('O produto ficara no valor de R$ {:.2f}'.format(produto + (produto * 20/100)))
