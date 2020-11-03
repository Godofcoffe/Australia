from time import sleep


print('='*40)
inicio = str(input('Deseja iniciar a contagem?: [S/N] ')).lower().strip()
if inicio == 's':
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    sleep(1)
    print('CHABLAU!!!')
elif inicio == 'n':
    print('Ok nos vemos na proxima.')
else:
    print('Digite apenas [ S ] ou [ N ]...')
