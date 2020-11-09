palavras = ('Cafe', 'sorvete', 'cocaina', 'chinelo', '"suc"', 'mafagafos', 'champola', 'Essencia de cavalo')
for p in palavras:
    print(f'Na palavra \033[33m{p.upper()}\033[m temos essas vogais: ', end=' ')
    for letra in p:
        if letra == 'a':
            print(f'\033[33m{"a"}\033[m', end=' ')
        if letra == 'e':
            print(f'\033[33m{"e"}\033[m', end=' ')
        if letra == 'i':
            print(f'\033[33m{"i"}\033[m', end=' ')
        if letra == 'o':
            print(f'\033[33m{"o"}\033[m', end=' ')
        if letra == 'u':
            print(f'\033[33m{"u"}\033[m', end=' ')
    print('')
