#Cria uma matriz 3x3, depois mostra a soma dos pares,
#a soma dos valores da terceira coluna e o maior da segunda linha. 

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha = []
pares = 0
print('=-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            pares += valor
for c in range(0, 3):
    linha.append(matriz[1][c])
print('=-='*15)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')
print('=-='*15)
coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {coluna}')
print(f'O maior valor da segunda linha é: {max(linha)}')
print('=-='*15)
