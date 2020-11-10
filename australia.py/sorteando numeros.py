from random import randint

n1 = randint(1, 5)
n2 = randint(1, 5)
n3 = randint(1, 5)
n4 = randint(1, 5)
n5 = randint(1, 5)
sorteados = (n1, n2, n3, n4, n5)
print(f'Foram sortados {sorteados}')
print(f'O maior é {sorted(sorteados)[-1]}')
print(f'E o menor é {sorted(sorteados)[0]}')
