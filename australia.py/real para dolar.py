try:
    real = float(input('R$:'))
except ValueError:
    print(f'Digite uma quantia valida.')
    real = float(input('R$:'))

while len(str(real)) > 5:
    print('Quantia não reconhecida, digite novamente com "." para  separar os centavos')
    real = float(input('R$:'))

print(f'Voce pode comprar {real/5.64:.2f} dolares')
print(f'E pode comprar tambem {real/6.61:.2f} euros')
