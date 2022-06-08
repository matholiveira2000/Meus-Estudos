from time import sleep
carro = float(input('Qual foi a velocidade do seu carro: '))
multa = (carro-80) * 7
print('Aguarde um momento...')
sleep(3)
if carro <= 80:
    print('Tudo certo tenha uma otima viagem')
else:
    print('Multa por limite excedido no valor de R${:.2f}'.format(multa))

