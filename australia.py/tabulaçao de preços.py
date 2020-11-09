produtos = ('Pão', 0.30, 'Leite', 4.00, 'Macarrão', 3, 'Boneca Inflavel', 10, 'Café Genérico', 50)
print('-'*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-'*40)
tam = len(produtos)
for c in range(0, tam, 2):
    print(f'{produtos[c]:.<30}R${float(produtos[c+1]):>8.2f}')
print('-'*40)
