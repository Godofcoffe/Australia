"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. """
nuns = list()
while True:
    entrada = int(input('Número: '))
    if entrada in nuns:
        print(f'Número ja existente...')
    else:
        nuns.append(entrada)
    opc = input('Quer continuar? [s/n]: ').lower().strip()[0]
    if opc == 'n':
        break
    elif opc == 's':
        pass
    else:
        print('opçao invalida')
print('Voce digitou esse numeros: ')
crescente = nuns[:]
crescente.sort()
for n in crescente:
    print(n, end=' ')
