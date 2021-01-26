alunos = []
while True:
    aluno = []
    nota = []
    nome = str(input('nome do aluno: '))
    aluno.append(nome)
    n1 = float(input('nota1: '))
    n2 = float(input('nota2: '))
    nota.append(n1)
    nota.append(n2)
    aluno.append(nota)
    alunos.append(aluno)
    fim = str(input('Continuar... [s/n]: ')).strip().lower()[0]
    if fim == 'n':
        break

print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
No.   NOME      MÉDIA
-------------------------------
""")
c = 1
for alun in alunos:
    print(f'{c} {alun[0]:^12} {alun[1][0] + alun[1][1] / 2:>4}')
    c += 1
print('-'*30)
while True:
    opc = int(input('Deseja ver a nota de que aluno? [999]encerra:  '))
    if opc == 999:
        break
    else:
        print(f'As notas do aluno {alunos[opc-1]}...')
