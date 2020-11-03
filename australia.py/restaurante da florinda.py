"""Exercício Python 43: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""
from time import sleep

print(f'{"Restaurante FLORINDA":=^43}')
preco = float(input('Qual o valor da conta? R$'))

while True:
    confirm = str(input(f'O valor registrado foi de R${preco:.2f}...\nConfirma? [S/N] ')).strip().lower()
    if confirm == 's':
        break
    else:
        preco = float(input('Qual o valor da conta? R$'))

print('Como deseja prosseguir o pagamento?:')
sleep(0.5)
print('[ 1 ] á vista dinheiro/cheque')
sleep(0.5)
print('[ 2 ] á vista no cartão')
sleep(0.5)
print('[ 3 ] 2X no cartão')
sleep(0.5)
print('[ 4 ] 3X no cartão')
sleep(3)
escolha = str(input('Sua opção?:')).strip()
if escolha == '1':
    descont = preco - (preco * 10 / 100)
    print(f'\nCom o valor de R${preco:.2f} no dinheiro/cheque, terá um desconto para R${descont:.2f}')

elif escolha == '2':
    descont = preco - (preco * 5 / 100)
    mensal = descont / 2
    print(f'\nCom o valor de R${preco:.2f} no cartão á vista, '
          f'você terá um desconto para R${descont:.2f}')

elif escolha == '3':
    mensal = preco / 2
    print(f'\nPara o pagamento de 2x no cartão, a mensalidade sairá por R${mensal:.2f} sem direito a desconto.')

elif escolha == '5':
    print('Se deseja parcelar por 3x no cartão ou mais digite o número de meses.')
    quant = int(input('Para o padrão de 3x no cartão apenas pressione [ Enter ]:'))

    if not bool(quant):
        juros = preco / 3 + (preco * 20 / 100)
        print(f'\nPela escolha padrão de 3x no cartão, o valor mensal sairá por R${juros:.2f}')

    elif quant > 3:
        juros = preco / quant + (preco * 20 / 100)
        print(f'\nPara {quant}x no cartão, o valor mensal sairá por R${juros:.2f}')

    else:
        pass

else:
    print(f'\033[1;31m{"Escolha uma opção valida!!!"}\033[m')
