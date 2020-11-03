termo = int(input('Quantos termos deseja?: '))
termo1 = 0
termo2 = 1
cont = 3
print(f'{termo1} -> {termo2}', end='')
while cont <= termo:
    termo3 = termo1 + termo2
    print(f' -> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' -> cabousi')
