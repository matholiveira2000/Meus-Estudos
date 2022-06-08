atual = 2021
na = int(input('OLA DIGITE O ANO DO SEU NASCIMENTO: '))
c = atual - na
if c < 9:
    print('COM SUA IDADE DE {} ANOS, VOCÊ SERA UM ATLETA MIRIM'.format(c))
elif c <= 14:
    print('COM A SUA IDADE DE {} ANOS, VOCE SERA UM ATLETA INFANTIL'.format(c))
elif c <= 19:
    print('COM A SUA IDADE DE {} ANOS, VOCÊ SERA UM ATLETA JUNIOR'.format(c))
elif c <= 25:
    print('COM A SUA IDADE DE {} ANOS, VOCE SERA UM ATLETA SENIOR'.format(c))
else:
    print('COM A SUA IDADE DE {}ANOS, VOCÊ SERA UM ATLETA MASTER'.format(c))

