"""
Irá ler a ano de nascimento de 8 pessoas e dizer quais são maiores de 18.
"""
from datetime import date


menores = 0
maiores = 0
for c in range(1, 8):
    pessoa_ano = int(input(f'Em que ano a {c}° nasceu: '))
    if date.today().year - pessoa_ano < 18:
        menores += 1
    else:
        maiores += 1
print(f'Nesta lista {menores} são menores.\nE {maiores} são maiores de idade.')
