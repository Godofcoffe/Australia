"""
somar numeros; flag 999
"""
somaTUDO = 0
quantos = 0
while True:
    n = int(input('Numero: '))
    if n == 999:
        break
    else:
        somaTUDO += n
        quantos += 1
print(f'A soma de tudo foi de {somaTUDO}')
print(f'E voce digitou {quantos} números.')
