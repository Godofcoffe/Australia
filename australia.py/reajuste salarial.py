"""
Se o salario for maior que 1250 terá um aumento de 10%, salario menor de 15%.
"""
print(40*'/')
sal = float(input('Digite seu salario:'))
if sal >= 1250:
    pcg = sal*10/100
    print(f'O seu reajuste será para R${sal+pcg}')
else:
    pcg = sal*15/100
    print(f'Seu reajuste será para {sal+pcg}')
