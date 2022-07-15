#Ler valores, perguntando o usuário quando parar.
#Por fim, mostra a lista de valores registrados.

lista = []
opcao = 'S'
print('=-='*15)
while True:
    if opcao in 'Nn':
        break
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado! Não será adicionado.')
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip()
        if opcao in 'Ss':
            break
        elif opcao in 'Nn':
            break
        else:
            print('Opção inválida.')
print('=-='*15)
print(f'Você digitou os valores: {lista}')
print('=-='*15)
