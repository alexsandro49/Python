#Mostra o maior e menor peso, dentre 5 lidos.

for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg')
print(f'O menor peso foi {menor}Kg')
