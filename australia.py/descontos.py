print(f'{"GERADOR DE DESCONTOS":.^60}')
produto = str(input('Nome do produto:'))
preco = float(input(f'Digite o preço do/a {produto}:'))

opc = int(input('[ 1 ] A vista\n[ 2 ] Parcelado\n-->: '))
if opc == 1:
    des = float(input('Digite o desconto %: '))
    valor = preco*des/100
    print(f'O valor de produto:{produto} = R${preco} com o desconto de {des:.2f}% será a partir de R${preco-valor:.2f}')
elif opc == 2:
    des = float(input('Digite o desconto %: '))
    valor = preco*des/100
    parc = int(input('Quantas vezes ?: '))
    print(f'O valor do produto {produto} = R${preco} com o desconto de {des:.2f}%, '
          f'parcelado em {parc} meses será a partir de R${preco/parc-valor:.2f}')
