#Simula um jogo de dados com 4 jogadores, 
#mostrando um ranking pelos pontos tirados.

from random import randint
from time import sleep
from operator import itemgetter
print('=-='*10)
dado = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador4': randint(1, 6) }
ranking = []
for k, v in dado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('=-='*10)
print('{:^30}'.format('RANKING DOS JOGADORES'))
print('=-='*10)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('=-='*10)
