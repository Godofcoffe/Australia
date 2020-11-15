from time import sleep

# número de notas disponivel no caixa...
caixa = {'notas50': 1000,
         'notas20': 1000,
         'notas10': 1000,
         'notas1': 1000}


def valid(tot, nota, cx, var_nota=0):
    for c in range(0, cx):
        if tot < nota:
            break
        if cx == 0 and tot >= nota:
            print(f'Acabaram as notas de {nota}...')
            break
        else:
            tot -= nota
            var_nota += 1
            cx -= 1
    if var_nota > 0:
        print(f'> {var_nota:>2} nota(s) de {nota}')
    return tot, cx


print('-' * 40)
print('SAIDINHA DE BANCO.PY')
print('-' * 40)
try:
    n = int(input('Quanto quer sacar? '))
except KeyboardInterrupt:
    print(f'\n\n\n\033[1;31m{"ENCERRANDO..."}\033[m')
    sleep(2)
else:
    while True:
        total = n
        if n > 1000:
            print(f'\033[33m{"O VALOR MAXIMO DE SAQUE É DE R$1.000..."}\033[m')
        else:
            while total > 0:
                print('SACANDO...')
                sleep(1)
                if caixa['notas50'] == 0:
                    print('Notas de 50 insuficientes!\n')
                else:
                    total, caixa['notas50'] = valid(total, 50, caixa['notas50'])

                if caixa['notas20'] == 0:
                    print('Notas de 20 insufifientes!\n')
                else:
                    total, caixa['notas20'] = valid(total, 20, caixa['notas20'])

                if caixa['notas10'] == 0:
                    print('Notas de 10 insuficientes!\n')
                else:
                    total, caixa['notas10'] = valid(total, 10, caixa['notas10'])

                if caixa['notas1'] == 0:
                    print('Notas de 1 insufucientes!\n')
                else:
                    total, caixa['notas1'] = valid(total, 1, caixa['notas1'])
                print('')

        sleep(5)

        try:
            sair = bool(input('Presione ENTER para FECHAR... '))
        except KeyboardInterrupt:
            print(f'\n\n\n\033[1;31m{"ENCERRANDO..."}\033[m')
            sleep(2)
            break
        else:
            print(f'\n\n\n\033[1;33m{"Volte Sempre..."}\033[m')
            sleep(3)

        print('\n\n\n')
        print('-' * 40)
        print('SAIDINHA DE BANCO.PY')
        print('-' * 40)
        try:
            n = int(input('Quanto quer sacar? '))
        except KeyboardInterrupt:
            print(f'\n\n\n\033[1;31m{"ENCERRANDO..."}\033[m')
            sleep(2)
            break
