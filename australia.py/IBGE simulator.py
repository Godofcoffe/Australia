"""
Exibe quantas pessoas são maiores de 18 anos, quantos são homens e quantas mulheres são menores de 20 anos.
"""
print(f'{"cadastramento":=^30}'.upper())
maior18 = 0
mulheres = 0
homens = 0
opc = False
while True:
    try:
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
        idade = str(input('Idade: ')).strip()
        idade = int(idade)
        if idade >= 18:
            maior18 += 1
        if sexo == 'm':
            homens += 1
        if sexo == 'f' and idade < 20:
            mulheres += 1

    except ValueError:
        print('Algum dado está incorreto, tente de novo...')
    else:
        opc = bool(input('Digite ENTER para CONTINUAR ou QUALQUER TECLA para CANCELAR... '))
        if opc:
            break
        else:
            pass
print('.' * 40)
print(f'O total de pessoas maiores de 18 anos foi {maior18}')
print(f'{homens} foram homens.')
print(f'E {mulheres} mulher(es) era(m) menor(es) de 20 anos.')
