matriz = []
for c in range(0, 3):
    lista = []
    for d in range(0, 3):
        print(f'coluna [{c}]', end=' ')
        print(f'linha [{d}]', end=' ')
        lista.append(int(input('numero: ')))
    matriz.append(lista)

print('esse é o resultado...')
print(matriz[0])
print(matriz[1])
print(matriz[2])
