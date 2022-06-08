from time import sleep
print('\033[1;34;44 m OLA SEJA BEM VINDO A CENTRAL DE FINANCIAMENTO DA CAIXA ')
print('\033[1;33;44 m AGUARDE UM MOMENTO....')
sleep(3)
salario = float(input('\033[0;0;0 m Por favor diga o valor do seu salario mensal: R$ '))
casa = float(input('Qual o valor da casa: R$ '))
anos = int(input('Quantos anos de investimento você deseja: '))
p = casa / (anos * 12)
print('ESTAMOS SIMULANDO O SEU FINANCIAMENTO AGUARDE POR ALGUNS SEGUNDOS')
sleep(5)
if p > (salario * 30 / 100):
    print('\033[1;31;44 m DESCULPE MAS NÃO PODEMOS FAZER ESSE INVESTIMENTO NO MOMENTO TENTE NOVAMENTE DAQUI 90 DIAS')
else:
    print('\033[1;32;44 m Tenho uma boa noticia para você!!!')
    print('\033[1;32;44 m O seu financiamento foi aprovado para a sua casa em {} anos no valor de R$ {:.2f}'.format(anos, p))
print('\033[1;34;44 m ATÉ LOGO')

