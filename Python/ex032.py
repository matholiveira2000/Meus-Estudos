s = float(input('Salario do funcionario R$ '))
if s <= 1250:
    novo = s + (s * 15 / 100)
    print('O seu salario novo é de R$ {}'.format(novo))
else:
    n = s + (s * 10 / 100)
    print('O seu salario novo é de R$ {}'.format(n))

