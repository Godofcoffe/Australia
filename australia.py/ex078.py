"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
for c in range(0, 5):
    lista.append(str(input(f'manda o {c}° numero numero: ')))

pos = lista[:]
lista.sort()
maior = lista[-1]
menor = lista[0]
print(f'O maior foi o numero {maior} na posição ', end='')
for i, v in enumerate(pos):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor foi o numero {menor} na posição ', end='')
for i, v in enumerate(pos):
    if v == menor:
        print(f'{i}...', end='')
