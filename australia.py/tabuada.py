"""
Use um número negativo para para o loop.
"""
c = 1
while True:
    print('-' * 60)
    n = int(input('Digite um número para eu te dizer a tabuada: '))
    print('-' * 60)
    c = 1

    if n < 0:
        break
    while c <= 10:
        print(f'{n} X {c:>2} = {n * c:>2}')
        c += 1
print('finish')
