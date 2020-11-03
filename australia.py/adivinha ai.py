from random import randint

n_cpu = randint(0, 10)
tent = 1
print('='*32)
print('Pensei em um numero,adivinha ai.')
opc = int(input(': '))
while opc != n_cpu:
    print('!'*27)
    print('meu numero é indescubrivel.\nTenta ai de novo.')
    opc = int(input(': '))
    tent += 1
print('-'*32)
print(f'Voce acertou com {tent} tentativas.')
print('Para...bens.')
