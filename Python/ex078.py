palavras = ('Metallica', 'Megadeth', 'Slayer', 'Sepultura',
            'Black Sabbath', 'The Who', 'Led Zeppelin')
for b in palavras:
    print(f'\nNa palavra {b.upper()} temos', end='')
    for letra in b:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
