def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} o voto não é permitido'
    elif idade <= 16 or idade < 18 or idade > 65:
        return f'Com {idade} de idade o voto é opcional'
    else:
        return f'Com {idade} de idade o voto é obrigatorio'


print(voto(1948))
