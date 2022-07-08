#Mostra quantos números foram digitados, e a soma deles.

opcao = 1
numeros = soma = 0
while opcao != 0:
    opcao = int(input('Digite um número [0 para o programa]: '))
    numeros += 1
    soma += opcao
numeros -= 1
print(f'Você digitou {numeros} números e a soma entre eles foi {soma}.')
