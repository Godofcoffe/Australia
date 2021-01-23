numeros = list()
pares = []
impares = []
for c in range(0, 7):
    n = int(input(f'{c}° numero: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    numeros.append(pares)
    numeros.append(impares)
pares = sorted(pares)
impares = sorted(impares)
print(f'Esses sao os numeros pares {numeros[0]}')
print(f'Esses sao os numeros impares {numeros[1]}')
