#Escolhe um número entre 0 e 5 e pede pro usuário adivinhar.

from random import randint

print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
escolhido = randint(0, 5)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

if numero == escolhido:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print(f'GANHEI! Pensei no número {escolhido} e não no {numero}!')
