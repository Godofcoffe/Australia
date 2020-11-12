nota = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota + nota2 + nota3 + nota4) / 4
print(f'Com as notas {nota}, {nota2}, {nota3} e {nota4} e com a media {media}')
print('O aluno esta:')
if media < 5:
    print('REPROVADO!')
elif 5 <= media <= 6.9:
    print('RECUPERAÇAO!')
else:
    print('APROVADO!')
