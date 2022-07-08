#Mostra a sequência de Fibonacci, 
#com a quantidade de termos escolhida pelo usuário.

print('=-'*15)
print('    Sequência de Fibonacci    ')
print('=-'*15)
termos = int(input('Número de termos: '))
print('=-'*15)
p1 = 0
p2 = 1

print(f'{p1} -> {p2} ->', end=' ')
for c in range(2, termos):
    p3 = p1 + p2
    print(f'{p3} ->', end=' ')
    p1 = p2
    p2 = p3
print('FIM')
