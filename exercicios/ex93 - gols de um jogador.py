#Mostra os dados de um jogador, com o nome, gols e partidas.

dados = {}
lista_gols = []
total = 0

print('=-='*10)
dados['nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {dados["nome"]}, fez? '))
print('=-='*10)

for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    lista_gols.append(gols)
    total += gols 

dados['gols'] = lista_gols[:]
dados['total'] = total[:]
print('=-='*10)
print(dados)
print('=-='*10)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('=-='*10)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, len(lista_gols)):
    print(f'Na partida {c}, fez {lista_gols[c]} gols.')
print(f'Foi um total de {total} gols.')
print('=-='*10)
