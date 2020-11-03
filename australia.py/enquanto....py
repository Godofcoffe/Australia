from time import sleep

sexo = str(input('digite seu sexo: [M/F] '))

while True:
    if sexo == 'j':
        print('Então voce é um JABUTI...')
        sleep(3)
    if sexo != 'm' and sexo != 'f':
        print('tente de novo.')
        sexo = str(input('Digite seu sexo: [M/F] '))
    else:
        break
print('acabou!')
