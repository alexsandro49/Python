#Jokenpo com o computador

from time import sleep
from random import choice

print('Suas opções:')
print('[0] - PEDRA')
print('[1] - PAPEL')
print('[2] - TESSOURA')
jogador = int(input('Sua jogada: '))

print('JO')
sleep(0.1)
print('KEN')
sleep(0.1)
print('PO!!!')
sleep(0.1)

opcoes = [0, 1, 2]
computador = choice(opcoes)
sleep(0.1)

if computador == 0 and jogador == 2:
    placar = 'COMPUTADOR VENCEU!'
    resultado0 = 'PEDRA'
    resultado1 = 'TESSOURA'
elif computador == 1 and jogador == 0:
    placar = 'COMPUTADOR VENCEU!'
    resultado0 = 'PAPEL'
    resultado1 = 'PEDRA'
elif computador == 2 and jogador == 1:
    placar = 'COMPUTADOR VENCEU!'
    resultado0 = 'TESSOURA'
    resultado1 = 'PAPEL'
elif jogador == 0 and computador == 2:
    placar = 'JOGADOR VENCEU!'
    resultado0 = 'TESSOURA'
    resultado1 = 'PEDRA'
elif jogador == 1 and computador == 0:
    placar = 'JOGADOR VENCEU!'
    resultado0 = 'PEDRA'
    resultado1 = 'PAPEL'
elif jogador == 2 and computador == 1:
    placar = 'JOGADOR VENCEU!'
    resultado0 = 'PAPEL'
    resultado1 = 'TESSOURA'
elif jogador == 0 and computador == 0:
    placar = 'EMPATE!'
    resultado0 = 'PEDRA'
    resultado1 = 'PEDRA'
elif jogador == 1 and computador == 1:
    placar = 'EMPATE!'
    resultado0 = 'PAPEL'
    resultado1 = 'PAPEL'
elif jogador == 2 and computador == 2:
    placar = 'EMPATE!'
    resultado0 = 'TESSOURA'
    resultado1 = 'TESSOURA'

sleep(0.1)
print('-='*10)
print(f'COMPUTADOR jogou {resultado0}')
print(f'JOGADOR jogou {resultado1}')
print('-='*10)
sleep(0.1)
print(placar)
