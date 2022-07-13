#Ler vários valores, depois mostra a quantidades de elementos digitados,
#mostra no formato de uma lista decrescente, além de verificar se o valor 5 está entre eles. 

lista = []
opcao = 'S'
print('=-='*20)
while True:
    if opcao in 'Nn':
        break
    lista.append(int(input('Digite um valor: ')))
    while True:
        opcao = str(input('Deseja continuar? [S/N] '))
        if opcao in 'Nn':
            break
        elif opcao in 'Ss':
            break
        else:
            print('Opção inválida.')

print('=-='*20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
print('=-='*20)
