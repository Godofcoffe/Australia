from random import randint, choice, shuffle
from time import sleep

""" Invés de digitar o valor da velociaddes dos carros, pensei em automatizar e simular mais um radar, 
    como se ele estivese apenas mirando em direção a pista
"""

total = 0
quant = 0
rachador = 0
carro_disciplinado = 0
""" parte dos dados das placas"""
tmp = []
placas = []
letras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
letras = letras.upper()
letras = letras.split()
numeros = '0 1 2 3 4 5 6 7 8 9'
numeros = numeros.split()

try:
    while True:
        print(30*'-')
        dif = 0
        multa = 0
        vel_car = float(randint(0, 150))
        if vel_car > 80:
            print('{:/^40}'.format('  carro acima da velocidade  '))
            print(f'Velocidade registrada: {vel_car} KM/H')

            # gerador de placas
            tmp.clear()
            for c in range(0, 4):
                tmp.append(choice(letras))
            for c in range(0, 3):
                tmp.append(choice(numeros))
            shuffle(tmp)
            if ''.join(tmp) not in placas:
                placas.append(''.join(tmp))

            dif = vel_car - 80
            multa = 7 * dif
            total += multa
            quant += 1
            rachador += 1
            print(f'A multa será de R${multa:.2f}')
            # os sleeps são para separar os carros como se estivessem passando proximos um do outro,
            # ou distantes.
            sleep(randint(0, 3))
        else:
            print('tudo bem por enquanto...')
            carro_disciplinado += 1
            sleep(randint(0, 4))

except KeyboardInterrupt:
    print(80*'#')
    print(f'O total de multas hoje foi de {quant}, com o valor total de R${total:.2f}')
    print('{:*^40}'.format(' Número de carros '))
    print(f'RACHADORES: {rachador}')
    print(f'COMPORTADOS: {carro_disciplinado}')
    print(f'placas registradas dos rachadores:')
    for placa in placas:
        print(placa)
