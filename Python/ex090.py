a = {}
a['Aluno'] = str(input('Digite o Nome do aluno: '))
a['Media'] = float(input(f'Media de {a["Aluno"]}: '))
if a["Media"] < 6:
    print(f'A situação de {a["Aluno"]} é de reprovado')
else:
    print(f'A situação de {a["Aluno"]} é de aprovado')
