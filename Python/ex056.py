somaid = midh = totm20 = media = 0
nomehv = ''
for c in range(1, 5):
    print(f'--------{c} PESSOAS -------')
    nome = str(input('Qual é o seu nome: '))
    id = int(input('Qual é a sua idade: '))
    sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    somaid += id
    if c == 1 and sex in 'Mm':
        midh = id
        nomehv = nome
    if sex in 'Mm' and id > midh:
        midh = id
        nomehv = nome
    if sex in 'Ff' and id < 20:
        totm20 += 1
media = somaid / 4
print(f' A media de idade do grupo é de {media}')
print(f'O homem mais velho do grupo tem {midh} anos e se chama {nomehv}')
print(f'Ao todo são {totm20} mulheres com menos de 20 anos')

