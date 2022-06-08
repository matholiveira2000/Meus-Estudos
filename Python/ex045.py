from random import randint
print('-'*50)
print('BEM VINDO AO JOKENPÔ')
print('-'*50)
print('ESCOHA UMA DAS OPÇÕES ABAIXO')
e = int(input('''
[ 1 ] PEDRA              
[ 2 ] PAPEL 
[ 3 ] TESOURA 
:  '''))
c = randint(1, 3)
if e ==1 and c == 2:
    print('VOCE ESCOLHEU PEDRA, E O PC ESCOLHEU PAPEL, OU SEJA VOCÊ PERDEU!!!')
elif e ==1 and c == 3:
    print('VOCÊ ESCOLHEU PEDRA, E O PC ESCOLHEU TESOURA, VOCÊ VENCEU!!!')
elif e ==1 and c ==1:
    print('AMBOS ESCOLHERAM PEDRA, HOUVE UM EMPATE')
elif e ==2 and c ==1:
    print('VOCÊ ESCOLHEU PAPEL, E O PC ESCOLHEU PEDRA. OU SEJA VOCÊ GANHOU!!!')
elif e ==2 and c==3:
    print('VOCÊ ESCOLHEU PAPEL, E O PC ESCOLHEU TESOURA. OU SEJA VOCÊ PERDEU!!!')
elif e ==2 and c ==2:
    print('AMBOS ESCOLHERAM PAPEL. HOUVE UM EMPATE')
elif e == 3 and c == 1:
    print('VOCÊ ESCOLHEU TESOURA, E O PC ESCOLHEU PEDRA. OU SEJA VOCÊ PERDEU!!!')
elif e == 3 and c == 2:
    print('VOCÊ ESCOLHEU TESOURA, E O PC PAPEL. OU SEJA VOCÊ GANHOU!!!')
else:
    print('AMBOS ESCOLHERAM TESOURA, HOUVE UM EMPATE')
