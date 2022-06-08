ficha = []
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    b = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    if b == 'N':
        break
print('-='*35)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    op = int(input('Qual nota do aluno mostrar? [999 para interromper] '))
    if op == 999:
        print('FIM')
        break
    if op <= len(ficha) - 1:
        print(f'Notas do aluno {ficha[op][0]} são {ficha[op][1]}')


