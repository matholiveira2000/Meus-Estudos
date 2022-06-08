print('\033[0;32;0 m *'*100)
print('\033[1;0;0 m PATRIA AMADA BRASIL ')
print('\033[0;33;0 m *'*100)
print('\033[0;0;0 m OLA SEJA BEM VINDO A CENTRAL DE ALISTAMENTO MILITAR')
print('.'*100)
alistamento = int(input('\033[0;0;0 m Por favor nos informe o ano que você nasceu: '))
ano = 2021
t = ano - alistamento
if t == 18:
    print('''QUEM NASCEU EM {} TEM {} ANOS EM {}
VOCE TEM QUE SE ALISTAR NESTE ANO'''.format(alistamento, t, ano))
elif t > 18:
    print('''QUEM NASCEU EM {} TEM {} ANOS EM {}
 VOCE TEM QUE SE ALISTAR IMEDIATAMENTE'''.format(alistamento, t, ano))
elif t < 18:
    print('''QUEM NASCEU EM {} TEM {} ANOS EM {}
 AINDA FALTA {} ANOS PARA VOCE SE ALISTAR'''.format(alistamento, t, ano, 18 - t))
print('-'*100)
print('ATE LOGO')
print('-'*100)
