"""
Exibe quantos produtos são maiores de R$1.000 e qual o mais barato
"""

print('-' * 50)
print('ESTATISTICAS DE PRODUTOS')
total = 0
mais_caros = 0  # mais de 1000
mais_barato = 0
n_barato = ''
while True:
    produto = str(input('Nome de produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    total += preco
    if preco > 1000:
        mais_caros += 1
    if mais_barato == 0:
        mais_barato = preco
        n_barato = produto
    if preco < mais_barato:
        mais_barato = preco
        n_barato = produto
    parada = str(input('Quer continuar? [S/N] '))
    if parada in 'Sims':
        pass
    if parada in 'Naon':
        break

print(f'O total foi de R${total:.2f}')
print(f'Teve {mais_caros} produtos mais caros que R$1.000.')
print(f'O produto mais barato foi {n_barato} com o valor de R${mais_barato:.2f}')
