from time import sleep


print(f'{"CALCULATION":=^40}')
num1 = int(input('Numero 1: '))
num2 = int(input('numero 2: '))
while True:
    print('-' * 32)
    print('Oque voce quer fazer?')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair')
    opc = int(input('Sua opção: '))
    if opc == 1:
        print(f'A soma de {num1} com {num2} foi de resultou em {num1+num2}')
    elif opc == 2:
        print(f'O produto de {num1} e {num2} foi de {num1*num2}')
    elif opc == 3:
        if num2 > num1:
            print(f'O {num1} é menor que {num2}')
        else:
            print(f'O {num2} é maior que {num1}')
    elif opc == 4:
        num1 = int(input('Redefinir o primero numero por: '))
        num2 = int(input('Redefinir o segundo numero por: '))
    elif opc == 5:
        break
    sleep(2)
print('Obrigado por usar o CALCULATOR!')
