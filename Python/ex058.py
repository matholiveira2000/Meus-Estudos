from random import randint
pc = randint(1, 10)
print('Ola vamos jogar um jogo de adivinhações')
print('Duvido você acertar')
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Qual é o seu palpite: '))
    palpites += 1
    if jogador == pc:
        acerto = True
    else:
        if jogador < pc:
            print('Errou! mais')
        elif jogador > pc:
            print('Errou! menos')
print(f'Acertou com {palpites} tentativas')

