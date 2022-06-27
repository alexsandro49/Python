#Solicita 3 valores, destacando o meno e o maior valor.

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {menor:.1f}')
print(f'O maior valor digitado foi {maior:.1f}')
