exp = str(input('DIgite a expressao: '))
if exp.count('(') == exp.count(')'):
    print('Não a parenteses faltando')

for s in exp:
    if s in '+-*/':
        p = exp.index(s)
        n1 = exp[p - 1]
        n2 = exp[p + 1]
        if not n1.isalnum() and not n2.isalnum():
            print('algo de errado nao esta certo')

print(exp)
