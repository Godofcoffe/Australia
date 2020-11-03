from time import sleep

print('-' * 40)
print('SAIDINHA DE BANCO.PY')
print('-' * 40)
n = int(input('Quanto quer sacar? '))
total = 0
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    if total > n - 50:
        while True:
            if total > n - 20:
                while True:
                    if total > n - 10:
                        while True:
                            if total > n - 1:
                                break
                            else:
                                total += 1
                                n1 += 1
                        break
                    else:
                        total += 10
                        n10 += 1
                break
            else:
                total += 20
                n20 += 1
        break
    else:
        total += 50
        n50 += 1
print('\n')
print('=' * 40)
print(f'No valor solicitado de R${n:.2f}!')
print(f'Seram entreges:\n')
print(f'> {n50:>2} nota(s) de 50\n> {n20:>2} nota(s) de 20\n> {n10:>2} nota(s) de 10\n> {n1:>2} nota(s) de  1\n')
sleep(1)
input('Presione ENTER para fechar...')
print(f'\n\n\n\n\033[1;33m{"Volte Sempre..."}\033[m\n\n')
