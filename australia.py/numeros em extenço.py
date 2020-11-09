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
           'dieseseis',
           'diesesiete',
           'dieseocho',
           'diesenueve',
           'veinte')
entrada = int(input('Manda un numero ai entre 0 e 20: '))
while entrada > 20 or entrada < 0:
    entrada = int(input('ENTRE 0 E 20: '))

for pos, n in enumerate(numeros):
    if entrada == pos:
        print(f'Usted digitó el número {numeros[pos]}')
        print('espero que tenga un bueno dia!')
        print('Vuelve siempre')
