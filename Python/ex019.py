import random
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print('o aluno sorteado foi {}'.format(s))



