nome = str(input('Digite o seu nome: '))
id = int(input('Digite a sua idade: '))
sexo = str(input('sexo [M/F]: ')).upper()[0]
while sexo not in 'MmFf':
    print('Erro')
