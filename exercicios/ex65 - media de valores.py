#Coleta valores que o usuário digita, mostrando a quantidade, a média,
#o maior e o menor valor apresentado.

soma = contador = numero = 0
opcao = 's'

while opcao not in 'Nn':
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
print(f'Você digitou {contador} números e a média foi {soma / contador:.1f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
