from random import randint
n = int(input('Digite um numero entre 0 e 5, e tente descobrir qual numero o computador escolheu: '))
c = randint(0, 10)
if n == c:
    print('Parabens você acertou')
else:
    print('HAHAHAHA Você errou!!!')
print('Eu escolhi o numero {}'.format(c))
