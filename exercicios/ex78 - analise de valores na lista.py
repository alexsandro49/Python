#Ler 5 valores, mostrando a lista completa, maior e o menor valor
#nas suas respectivas posições na lista.

lista = []
print('=-='*12)
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-='*12)

lista_max = max(lista)
lista_min = min(lista)

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {lista_max} nas posições:', end=' ')
for i, c in enumerate(lista):
    if c == lista_max:
        print(f'{i}', end=' ')
print()
print(f'O menor valor digitado foi {lista_min} nas posições:', end=' ')
for i, c in enumerate(lista):
    if c == lista_min:
        print(f'{i}', end=' ')
print()
print('=-='*12)
