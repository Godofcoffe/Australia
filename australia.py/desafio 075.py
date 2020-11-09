numeros = ''
for c in range(0, 4):
    n = str(input('numero: '))
    numeros += n
numeros = tuple(numeros)
print(f'Voce digitou {numeros}')
print(f'\nNa tupla existe {numeros.count(9)} números "9".')
if '3' in numeros:
    print(f'De 0 a 3... O número 3 está na posição {numeros.index("3")}')
else:
    print(f'Não foi digitado nenhum numero 3.')
print('E esses são números pares:')
for n in numeros:
    if int(n) % 2 == 0:
        print(f'{n}', end=' ')
