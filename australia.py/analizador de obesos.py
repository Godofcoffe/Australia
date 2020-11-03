"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""
nome = str(input('Seu nome (para melhorar a experiencia):'))
alt = float(input('Sua Altura: (m)'))
peso = float(input('Seu peso: (Kg)'))
imc = peso / alt**2
if imc < 18.5:
    print(f'{nome} Com seu peso de {peso} e sua altura de {alt}, voce esta ABAIXO DO PESO')
elif imc < 25:
    print(f'{nome} com o seu peso em {peso} e sua altura em {alt}, voce esta no peso ideal')
elif imc < 30:
    print(f'{nome} com o seu peso em {peso} e sua altura em {alt}, voce esta em SOBREPESO')
elif imc < 40:
    print(f'{nome} com seu peso em {peso} e sua altura em {alt}, voce esta OBESO')
else:
    print(f'{nome} com o seu peso {peso} e sua altura {alt}, voce esta MUITO GORDO')
