#Verifica a validade de uma expressão pela quantidade de parentêses compatíveis.

conta = str(input('Digite uma expressão: '))
lista = []
for c in conta:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
