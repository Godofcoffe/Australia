init = str(input('Deseja iniciar?: ')).strip().lower()
maior = 0
menor = 0
centopeia_numerica = 0
cont = 0
while init == 's':
    n = int(input('Digite um número: '))
    centopeia_numerica += n
    cont += 1
    if n > maior:
        maior = n
    if menor == 0 and n > menor:
        menor = n
    if n < menor:
        menor = n
    init = str(input('Deseja continuar?: [S/N] ')).strip().lower()
# print(maior, menor)
print(f'A média entre os números foi {centopeia_numerica / cont:.1f}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
