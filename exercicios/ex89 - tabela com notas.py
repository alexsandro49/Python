#Monta uma tabela com os nomes e a média das notas,
#podendo mostrar todas as notas de um aluno específico.

lista = []
dados = []
opcao = 'S'

while True:
    if opcao in 'Nn':
        break
    nome = str(input('Nome: ')).strip()
    dados.append(nome)
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip()
        if opcao in 'Ss':
            break
        elif opcao in 'Nn':
            break
        else:
            print('Opção inválida.')
print('=-='*15)
print('{:<8}{:<15}{:<15}'.format('No.', 'Nome', 'Média'))
print('=-='*15)
for c in range(0, len(lista)):
    print('{:<8}{:<15}{:<15.2f}'.format(c, lista[c][0], (lista[c][1] + lista[c][2]) / 2))
print('=-='*15)
while True:
    selecao = int(input('Mostrar notas de qual aluno? (999 - finalizar) '))
    if selecao == 999:
        break
    elif selecao >= len(lista):
        print('Opção inválida.')
    else:
        print(f'Notas de {lista[selecao][0]}: {lista[selecao][1:]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE! >>>')
