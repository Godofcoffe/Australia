while True:
    dia = input('dia:')
    while len(dia) > 2 or int(dia) > 31 or bool(dia) == False:
        print('digite uma data valida')
        dia = input('dia:')

    mes = input('mes:')
    while len(mes) > 1 or int(mes) > 12 or bool(mes) == False:
        print('digite uma data valida')
        mes = input('mes:')

    ano = input('ano:')
    while len(ano) > 4 or len(ano) == 3 or len(ano) == 1 or bool(ano) == False:
        print('digite uma data valida')
        ano = input('ano:')

    print(f'{dia}/{mes}/{ano}')
