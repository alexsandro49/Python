#Mostra a soma entre os valores de 0 a 500 que são divisíveis por 3.

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma dos {cont} valores solicitados é {s}')
