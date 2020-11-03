# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.

dia = int(input('Dias de uso:'))
kms = float(input('Kilometros rodados:'))
total = dia*60 + kms*0.15
print(f'O total a pagar será de R${total:.2f}')
