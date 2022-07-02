#Cria uma tabuada usando o laço de repetição.

numero = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{numero} X {c} = {numero*c}')
