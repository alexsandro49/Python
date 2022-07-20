#Mostra uma tabela com informações de jogadores,
#permitindo uma visualição individual para cada atleta.

jogadores = []
jogador = {}
lista_gols = []
gols = []

print('=-='*10)
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))    
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    print('=-='*10)
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao not in 'SsNn':
        while True:
            print('Erro! Por favor, apenas S ou N.')
            opcao = str(input('Quer continuar? [S/N] '))
            if opcao in 'SsNn':
                break
    if opcao in 'Nn':
        break 
print('=-='*10)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*45)
for k, v in enumerate(jogadores):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-'*45)
print('=-='*10)

while True:
    busca = int(input('Mostra dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('Erro! Jogador inexistente.')
    else:
        print(f'    Dados do jogador {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
print('=-='*10)

