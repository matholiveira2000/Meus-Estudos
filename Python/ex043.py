altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)
print('O seu IMC é de {:.1f}'.format(imc))
if imc <18:
    print('VOCÊ ESTA ABAIXO DO PESO')
elif imc >=18.5 and imc <=25:
    print('VOCÊ ESTA NO PESO IDEAL')
elif imc >25 and imc <=30:
    print('VOCÊ ESTA COM SOBREPESO')
elif imc >30 and imc <=40:
    print('VOCÊ ESTA COM OBESIDADE')
else:
    print('VOCÊ ESTA COM OBESIDADE MORBIDA')
