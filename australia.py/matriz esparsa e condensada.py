"""
Uma matriz esparsa ´e uma matriz que tem diversos elementos iguais a zero, tal qual
mostrado abaixo a esquerda. Escreva um algoritmo que leia uma matriz M de 5×5
de valores inteiros, que seja supostamente esparsa e a partir dela organize uma matriz
condensada, de apenas 3 colunas, com apenas os elementos n˜ao nulos da matriz original.
A matriz condensada (mostrada abaixo a direita) ´e organizada de forma que em cada
linha dela se tenha:
• na primeira coluna, o valor n˜ao nulo de M;
• na segunda coluna, o ´ındice da linha de M, onde foi encontrado esse valor;
• na terceira coluna, o ´ındice da coluna de M, onde foi encontrado esse valor
"""
from random import randint
matriz_esparsa = []
matriz_condensada = []
for c in range(5):
    linha = []
    for c in range(5):
        linha.append(randint(0, 99))
    matriz_esparsa.append(linha)

print(matriz_esparsa)
for l, lin in enumerate(matriz_esparsa):
    for item in lin:
        linha = []
        if item > 0:
            linha.append(item)
            linha.append(l)
            linha.append(lin.index(item))
        matriz_condensada.append(linha)
            
for array in matriz_condensada:
    print(array)
