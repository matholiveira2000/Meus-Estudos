soma = cont = media = maior = menor = 0
q = 'SN'
while q != 'N':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    q = str(input('quer continuar? [S/N]  ')).upper().strip()[0]
media = soma / cont
print('você digitou {} e a media entre eles foi de {:.2f}'.format(cont, media))
print('O maior valor foi de {} e o menor valor foi de {}'.format(maior, menor))
