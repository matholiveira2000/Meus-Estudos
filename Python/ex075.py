from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print(f'Eu sorteei os valores {lista}')
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
