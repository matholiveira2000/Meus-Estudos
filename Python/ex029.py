from time import sleep
p = float(input('Qual sera a distancia da sua viagem ?: '))
print('você esta  prestes a iniciar uma viagem de {:.2f}Km'.format(p))
print('Aguarde enquanto calculamos a sua rota......')
sleep(3)
if p <= 200:
    print('valor da sua viagem deu R$ {:.2f}. TENHA UMA OTIMA VIAGEM!!'.format(p * 0.50))
else:
    print('OBA TEMOS UMA PROMOÇÃO PRA VOCÊ!!!')
    print('O valor da sua passagem fico R$ {:.2f}'.format(p * 0.45))
