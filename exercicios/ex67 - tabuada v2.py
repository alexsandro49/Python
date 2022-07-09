#Monta uma tabuada de um número escolhido pelo usuário.
#Números negativos fecham o programa.

print('=-'*10)
while True:
    numero = int(input('Tabuada do número: '))
    if numero < 0:
        print('=-'*10)
        break
    print('=-'*10)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('=-'*10)
print('Programa encerrado!')
