par = []
impar = []
print('Para o inicio da contagem, inicie com 1 para mostrar os impares e 2 para os pares.')
n1 = int(input('Digite o inico da contagem [ 1 ] [ 2 ]:'))
n2 = int(input('Digite o final da contagem:'))
for c in range(n1, n2+1, 2):
    if n1 == 2:
        par.append(c)
    elif n1 == 1:
        impar.append(c)
print(f'Com a contagem de {n1} a {n2}.')
if n1 == 2:
    print(f'Temos um total de {par} pares.')
elif n1 == 1:
    print(f'E temos o total de {impar} impares.')
