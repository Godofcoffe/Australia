pessoas = {}
lista_pesos = []
for c in range(1, 6):
    pessoa = str(input(f'Nome da {c}° pessoa: '))
    peso = float(input(f'Peso do(a) {pessoa}: KG'))
    pessoas[pessoa] = peso
for p in pessoas.values():
    lista_pesos.append(p)
lista_pesos.sort()
menor = lista_pesos[0]
maior = lista_pesos[-1]
n_maior = None
n_menor = None
for pessoa in pessoas.items():
    if menor in pessoa:
        n_menor = pessoa[0]
    elif maior in pessoa:
        n_maior = pessoa[0]
print(f'{n_maior} é a pessoa mais pesada, com {maior}Kg.')
print(f'{n_menor} é a pessoa mais leve, com {menor}Kg')
