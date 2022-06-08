n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media < 5:
    print('VOCÊ TIROU {} , FOI REPROVADO'.format(media))
elif media >= 5  and media < 7:
    print('VOCÊ TIROU {} , ESTA DE RECUPERAÇÃO ESTUDE MAIS!!!'.format(media))
elif media >=7:
    print('VOCÊ TIROU {} , ESTA APROVADO PARABENS!!!'.format(media))
