#Lista de preços numa tabela formatada, utilizando uma tupla.

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
lista = ('Lápis', 1, 'Caneta', 1.5, 'Caderno', 18,
         'Borracha', 0.5, 'Tessoura', 3.5)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end=' ')
    else:
        print(f'R${lista[c]:>5.2f}')
print('-'*40)
