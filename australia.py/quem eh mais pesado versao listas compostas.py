pessoas = list()
mais_pesadas = mais_leves = 0
pesadas = []
leves = []
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('peso: '))
    if mais_leves == 0 and mais_pesadas == 0:
        mais_pesadas = mais_leves = peso
    else:
        if peso > mais_pesadas:
            mais_pesadas = peso
        elif peso < mais_leves:
            mais_leves = peso
    pessoas.append([nome, peso])
    if not input():
        pass
    else:
        break
for p in pessoas:
    if mais_leves in p:
        leves.append(p[0])
    if mais_pesadas in p:
        pesadas.append(p[0])
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A mais leve é {leves}')
print(f'A mais pesada é {pesadas}')
