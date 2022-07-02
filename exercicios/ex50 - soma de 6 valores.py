#Ler 6 valores, somando apenas os pares.

s = 0
for c in range(0, 6):
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos valores pares é {s:.2f}')
