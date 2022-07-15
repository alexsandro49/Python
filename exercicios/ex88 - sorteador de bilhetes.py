#Sorteia bilhetes com 6 números (0-60), sem repetições de valores.

from random import randint

escolhidos = []
bilhetes = []
rodada = []
print('=-='*10)
print('{:^30}'.format('SORTEADOR DE BILHETES'))
print('=-='*10)
jogos = int(input('Número de jogos para gerar: '))
for c in range(1, jogos+1):  
    contador = 0
    while contador < 6:
        numero = randint(0, 60)
        if numero not in escolhidos:
            rodada.append(numero)
            escolhidos.append(numero)
            contador += 1
        else:
            continue
    bilhetes.append(rodada[:])
    rodada.clear()
    print(f'Jogo {c}: {bilhetes[c-1]}')
print('=-='*10)
