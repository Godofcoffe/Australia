numeros = ('cero',
           'uno',
           'dos',
           'tres',
           'cuatro',
           'cinco',
           'seis',
           'siete',
           'ocho',
           'nueve',
           'diez',
           'once',
           'doce',
           'treze',
           'catorze',
           'quinze',
           'diesiseis',
           'diesisiete',
           'diesiocho',
           'diesinueve',
           'veinte')
while True:
    entrada = int(input('Manda un numero ai entre 0 e 20: '))
    while entrada > 20 or entrada < 0:
        entrada = int(input('ENTRE 0 E 20: '))
    print(f'Voce escolheu o número {numeros[entrada]}')
    while True:
        esc = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if esc == 'n':
            break
        elif esc == 's':
            pass
        else:
            print('Eu sou uma piada para voce!?')
            esc = str(input('Quer continuar? SIM OU NÃO ')).strip().lower()[0]
