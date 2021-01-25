from random import randint
from time import sleep

print('-'*40)
print(f'{"PALPITES ERRONHOS PARA MEGA SENA":^40}')
print('-'*40)
palpites = []
quant = int(input('Quantos jogos: '))
for c in range(0, quant):
    temp = list()
    for d in range(0, 6):
        palp = randint(1, 60)
        if palp not in temp:
            temp.append(palp)
    palpites.append(temp)

for p in palpites:
    print(sorted(p))
    sleep(0.3)
