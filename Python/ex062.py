progressao = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = progressao
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= 10:
        print('{} - '.format(contador), end=' ')
        razao += progressao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos mostrar a mais: '))
print('FIM')
