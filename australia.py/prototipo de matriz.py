matriz = []
pares = 0
terc_colun = 0
for c in range(0, 3):
    lista = []
    for d in range(0, 3):
        print(f'coluna [{c}]', end=' ')
        print(f'linha [{d}]', end=' ')
        n = int(input('numero: '))
        lista.append(n)
        if n % 2 == 0:
            pares += n
        if d == 2:
            terc_colun += n
    matriz.append(lista)

print('esse é o resultado...')
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A soma dos pares se deu como {pares}')
print(f'A soma de todos da terceira coluna {terc_colun}')
print(f'{sorted(matriz[2])[2]} é o maior número da segunda linha')
