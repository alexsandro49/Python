#Lê valores, mostrando uma lista com todos os nḿeros digitados,
#uma só com os valores pares e outra com os ímpares.

lista = []
pares = []
impares = []
opcao = 'S'
print('=-='*15)
while True:
    if opcao in 'Nn':
        break
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0 and valor != 0:
        pares.append(valor)
    if valor % 2 != 0 and valor != 0:
        impares.append(valor)
    while True:
        opcao = str(input('Deseja continar? [S/N] '))
        if opcao in 'Ss':
            break
        elif opcao in 'Nn':
            break
        else:
            print('Opção inválida.')
print('=-='*15)
print(f'A lista completa é: {lista}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {impares}')
print('=-='*15)
