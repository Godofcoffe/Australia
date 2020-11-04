"""
Use um número negativo para para o loop.
"""

while True:
    print('-' * 60)
    n = int(input('Digite um número para eu te dizer a tabuada: '))
    print('-' * 60)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:>2} = {n*c:>2}')
print('finish')
