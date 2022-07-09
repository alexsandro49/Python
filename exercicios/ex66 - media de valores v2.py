#Ler valores que o usuário digitar, mostra a quantidade, a média,
#o maior e o menor valor apresentado. Usando a função break.

soma = contador = numero = 0

while True:
    numero = int(input('Digite um número: '))
    opcao = str(input('Deseja continar? [S/N]: '))
    if contador == 0:
        maior = menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    contador += 1
    soma += numero
    if opcao in 'Nn':
        break
print(f'Você digitou {contador} números e a média foi {soma / contador:.1f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
