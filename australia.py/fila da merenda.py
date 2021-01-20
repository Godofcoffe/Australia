"""
A hora mais esperada... dos guardas penitenciarios...
"""
from random import choice, shuffle

p1 = input('Nome:')
p2 = input('Nome:')
p3 = input('Nome:')
p4 = input('Nome:')
detentos = [p1, p2, p3, p4]
escolhido = choice(detentos)
print(f'A pessoa para ir na cadeira eletrica hoje será {escolhido}')
detentos.remove(escolhido)
shuffle(detentos)
print(f'Só sobraram {detentos} por enquanto...')
