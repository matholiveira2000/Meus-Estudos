dias = int(input('quantos dias usou o carro: '))
km = float(input('por quantos km vc andou com o carro:'))
pago = (dias * 60) + (km * 0.15)
print('o valor a ser pago é de R${:.2f}'.format(pago))
