from time import sleep

caixa = {'notas50': 1000,
         'notas20': 1000,
         'notas10': 1000,
         'notas1': 1000}

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
        n50 = 0
        n20 = 0
        n10 = 0
        n1 = 0
        while total > 0:
            print('SACANDO...')
            sleep(1)
            if caixa['notas50'] == 0:
                print('Notas de 50 insuficientes!\n')
            else:
                for c in range(0, caixa['notas50']):
                    if total < 50:
                        break
                    if caixa['notas50'] == 0 and total >= 50:
                        print('Acabaram as notas de 50...')
                        break
                    else:
                        total -= 50
                        n50 += 1
                        caixa['notas50'] -= 1
                if n50 > 0:
                    print(f'> {n50:>2} nota(s) de 50')

            if caixa['notas20'] == 0:
                print('Notas de 20 insufifientes!\n')
            else:
                for c in range(0, caixa['notas20']):
                    if total < 20:
                        break
                    if caixa['notas20'] == 0 and total >= 20:
                        print('Acabaram as notas de 20...')
                        break
                    else:
                        total -= 20
                        n20 += 1
                        caixa['notas20'] -= 1
                if n20 > 0:
                    print(f'> {n20:>2} nota(s) de 20')

            if caixa['notas10'] == 0:
                print('Notas de 10 insuficientes!\n')
            else:
                for c in range(0, caixa['notas10']):
                    if total < 10:
                        break
                    if caixa['notas10'] == 0 and total >= 10:
                        print('Acabaram as notas de 10')
                        break
                    else:
                        total -= 10
                        n10 += 1
                        caixa['notas10'] -= 1
                if n10 > 0:
                    print(f'> {n10:>2} nota(s) de 10')

            if caixa['notas1'] == 0:
                print('Notas de 1 insufucientes!\n')
            else:
                for c in range(0, caixa['notas1']):
                    if total < 1:
                        break
                    if caixa['notas1'] == 0 and total >= 1:
                        print('As notas de 1 acabaram...')
                        break
                    else:
                        total -= 1
                        n1 += 1
                        caixa['notas1'] -= 1
                if n1 > 0:
                    print(f'> {n1:>2} nota(s) de  1')
            print('')

        sleep(5)

        try:
            sair = bool(input('Presione QUALQUER TECLA para FECHAR...'))
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
