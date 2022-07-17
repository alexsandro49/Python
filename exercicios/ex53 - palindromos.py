#Testa se uma frase é um palíndromo.

frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
junto = ''.join(separar)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
