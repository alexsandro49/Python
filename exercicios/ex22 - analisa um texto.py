#Analisa um texto.

from itertools import count

nome = str(input('Digite seu nome completo: '))
print('Analisando...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome)} letras.')
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras.')