print(50*'=')
dist = float(input('Qual a distancia da viagem?: KM'))
if dist < 200:
    print(f'O preço da viagem será de R${0.50 * dist}')
else:
    print(f'O preço da viagem será de R${0.45 * dist}')
