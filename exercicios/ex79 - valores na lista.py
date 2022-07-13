#Ler valores, perguntando o usuário quando parar.
#Por fim, mostra a lista de valores registrados.

lista = []
opcao = ''
print('=-='*15)
while True:
    valor = int(input('Digite um valor: '))
    opcao = ''
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado! Não será adicionado.')
    while opcao in '':
        opcao = str(input('Quer continuar? [S/N] ')).strip()
        if opcao in 'Ss':
            continue
        elif opcao in 'Nn':
            break
        else:
            print('Opção inválida.')
            opcao = ''
    if opcao in 'Nn':
        break
print('=-='*15)
print(f'Você digitou os valores: {lista}')
print('=-='*15)
