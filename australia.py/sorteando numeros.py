from random import randint

n1 = str(randint(1, 5))
n2 = str(randint(1, 5))
n3 = str(randint(1, 5))
n4 = str(randint(1, 5))
n5 = str(randint(1, 5))
sorteados = (n1, n2, n3, n4, n5)
print(sorteados)
menor = sorted(sorteados)[0]
maior = sorted(sorteados)[-1]
print(f'O maior é {maior}')
print(f'E o menor é {menor}')
