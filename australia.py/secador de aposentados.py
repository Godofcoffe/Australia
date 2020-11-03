print('='*40)
nome = str(input('Seu nome:'))
slr = float(input('Seu salario:'))
valor_casa = float(input('Valor da casa:'))
parcelas = int(input('Por quantos anos?:')) * 12
porcentagem_min = slr*30/100
recomendado = 0

if valor_casa/parcelas > porcentagem_min:
    print(f'Emprestimo negado por salário de R${slr:.2f} e {parcelas} parcelas mensais não compativeis!')
    for c in range(1, 300):
        if valor_casa / c <= porcentagem_min:
            recomendado = c
            break
        elif valor_casa / c > porcentagem_min:
            pass

    print(f'Com o salario de R${slr:.2f} recomendamos no minimo {recomendado} parcelas mensais')
else:
    print(f'Emprestimo confirmado Sr.{nome}, na casa do valor de R${valor_casa:.2f}')
    print(f'A mensalidade sairá por R${valor_casa/parcelas:.2f} por {parcelas} meses.')
