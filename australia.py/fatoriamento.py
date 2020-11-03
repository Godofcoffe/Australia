f = n = int(input('Numero:'))
produto = 1
while f > 1:
    print(f'{n}x{f}')
    produto = f * produto
    f -= 1
print(f'O fatorial foi de: {produto}')
