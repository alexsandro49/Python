#Mostra 5 valores sorteados, e a sua soma.

from random import randint
lista = []

def sortear(* num):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[c]}', end=' ')
    print('PRONTO!')
def somaPar():
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')


print('=-='*15)
sortear()
somaPar()
print('=-='*15)
