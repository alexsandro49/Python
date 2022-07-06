'''Pede pra escolher um numero entre 0 e 10, looping enquanto o usuário não acerta.
Indica se o número correto é maior ou menor ao escolhido, além de contar as tentativas'''

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
    elif n < computador:
        print('Mais... tente mais ma vez.')
    elif c > computador:
        print('Menos... tente mais uma vez.')

print(f'Acertou com {c} tentativas. Parabéns!')
