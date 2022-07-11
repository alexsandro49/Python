#Ler 4 valores, e mostra quantas vezes apareceu o número 9,
#a posição do número 3 e a quantidade de valores pares.

print('=-='*12)
n = (int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')), int(input('Digite um número: ')))
pares = valor9 = pos3 = 0
for c in range(0, 4):
    if n[c] % 2 == 0 and n[c] != 0:
        pares += 1
    if n[c] == 9:
        valor9 += 1
    if 3 in n:
        pos3 = n.index(3) + 1

print('=-='*12)
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {valor9} vezes')
print(f'O valor 3 apareceu na {pos3}ª posição.')
print(f'Os valores pares digitados foram {pares}')
print('=-='*12)
