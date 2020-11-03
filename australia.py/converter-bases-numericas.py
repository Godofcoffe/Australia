from time import sleep

print('{:.^80}'.format('conversor numérico.').upper())
init = bool(input('Pressione ENTER para INICIAR...'))
while not init:
    try:
        n = int(input('\nDigite um número...\nOu qualquer outra coisa para CANCELAR: '))
    except ValueError:
        break
    else:
        sleep(1)
        print('Para converter escolha uma opção abaixo...\n')
        sleep(1)
        print('[ 1 ] Binário')
        sleep(0.5)
        print('[ 2 ] Octal')
        sleep(0.5)
        print('[ 3 ] Hexadecimal\n')
        sleep(3)
        try:
            opc = int(input('Sua escolha: '))
        except ValueError:
            print(f'\033[31m{"ESCOLHA UMAS DAS 3 OPÇÕES APENAS!"}\033[m')
        else:
            sleep(2)
            if opc == 1:
                print(f'\n> \033[32m{bin(n)[2:]}\033[m <')
            elif opc == 2:
                print(f'\n> \033[32m{oct(n)[2:]}\033[m <')
            elif opc == 3:
                print(f'\n> \033[32m{hex(n)[2:]}\033[m <')
            print('-' * 40)
            init = bool(input('Pressione ENTER para continuar.\nOu qualquer tecla para fechar... '))
            # digite alguma coisa e de ENTER para fechar.
