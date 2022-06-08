nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Prazer em te conhecer!')
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))

