nota = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota + nota2) / 2
print(f'Com as notas {nota} e {nota2} e com a media {media}')
print('O aluno esta:')
if media < 5:
    print('REPROVADO!')
elif 5 <= media <= 6.9:
    print('RECUPERAÇAO!')
else:
    print('APROVADO!')
