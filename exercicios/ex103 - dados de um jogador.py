#Mostra os dados de um jogador, excluindo erros por dados vazios.

def ficha(n = '<<Desconhecido>>', g = 0):
    return f'O jogador {n} fez {g} gols no campeonato.'


print('=-='*15)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    print(ficha(g = gols))
else:
    print(ficha(nome, gols))
print('=-='*15)
