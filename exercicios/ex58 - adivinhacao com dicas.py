#Jogo de adivinhação com o computador, indicando se o número escolhido é maior ou menor
#No fim, mostra a quantidade de tentativas até o acerto.

from random import randint

c = 0
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10.')
print('Tente adivinhar que número foi...')
loop = True

while loop == True:
    c += 1
    n = int(input('Seu palpite: '))
    if n == computador:
        loop = False
    else:
        if n < computador:
            print('Mais... tente mais ma vez.')
        elif n > computador:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {c} tentativas. Parabéns!')
