ano = 2022
d = dict()
d['nome'] = str(input('Nome: ')).upper()
d['nascimento'] = int(input('Nascimento: '))
d['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
d['idade'] = ano - d['nascimento']
print('-=' * 50)
if d['ctps'] == 0:
    for k, v in d.items():
        print(f'- {k} tem o valor {v}')
else:
    d['contratação'] = int(input('Ano de contratação: '))
    d['salario'] = float(input('Salario: '))
    d['aposentadoria'] = d['contratação'] + 35
print('-=' * 50)
for i, l in d.items():
    print(f'- {i} Tem o valor {l}')

