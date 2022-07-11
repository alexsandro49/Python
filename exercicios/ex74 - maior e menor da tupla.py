#Sorteia 5 numeros em uma tupla, mostrando o maior e o menor deles.

from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}.')
print(f'O menor valor sorteado foi {min(n)}.')
