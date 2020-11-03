"""
Irá pedir 6 números e dizer quans são pares e soma-los.
"""
n = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c} número: '))
    if numero % 2 == 0:
        n += numero
        cont += 1
print(f'Entre seus números existe {cont} pares e seu somatorio é de {n}')
