#Lê 7 valores,listando os pares e os ímpares em uma ordem crescente.

lista = [[], []]
print('=-='*15)
maior = menor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0 and valor != 0:
        lista[0].append(valor)
    elif valor % 2 != 0 and valor != 0:
        lista[1].append(valor)
print('=-='*15)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')
print('=-='*15)
