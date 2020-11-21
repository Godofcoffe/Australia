print(f'{"DIVISORES":=^30}')
while True:
    print('\nDigite \033[1m0\033[m para fechar')
    num = int(input('Número: '))
    if num == 0:
        break
    print(f'\n\033[30mOs divisores do número {num} são...\033[m')
    for c in range(1, num + 1):
        if num % c == 0:
            print(f'\033[33m{c}\033[m ', end='')
    print('')
