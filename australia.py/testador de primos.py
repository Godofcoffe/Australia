print('MANDA UM NÚMERO AI...')
n = int(input('numero: '))
teste = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        teste += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')

if teste == 2:
    print(f'\nO número {n} foi dividido apenas 2 vezes.')
    print('Portanto...')
    print(f'{"Ele É primo":=^20}')
else:
    print(f'\nO número {n} foi dividido {teste} vezes.')
    print('Portanto...')
    print(f'{f"Ele NÃO é primo":=^21}')
