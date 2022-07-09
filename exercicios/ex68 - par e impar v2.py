#Jogo de par ou ímpar com o computador, acabando com a derrota do usuário.
#mostra o números de vitórias consecutivas.

from random import randint
vitorias = 0

print('=-'*12)
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).strip()
    computador = randint(1, 10)
    numero = jogador + computador
    print('=-'*12)
    if escolha in 'Pp' and numero % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. O total {numero} é um número PAR.')
        print('Você venceu!')
        print('=-'*12)
        vitorias += 1
    elif escolha in 'Pp' and numero % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. O total {numero} é um número ÍMPAR.')
        print('O computador venceu!')
        print('=-'*12)
        break
    elif escolha in 'Ii' and numero % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. O total {numero} é um número ÍMPAR.')
        print('Você venceu!')
        print('=-'*12)
        vitorias += 1
    elif escolha in 'Ii' and numero % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. O total {numero} é número PAR.')
        print('O computador venceu!')
        print('=-'*12)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')
print('=-'*12)
