#Mostra a metade, o dobro e um acréscimo de 10% de um número formatado como moeda,
#usando funcoes simplificadas em outro arquivo para uma melhor organização.

import funcoes

valor = float(input('Digite um valor: '))
print(f'A metade de {funcoes.moeda(valor)} é {funcoes.metade(valor, True)}')
print(f'O dobro de {funcoes.moeda(valor)} é {funcoes.dobro(valor, True)}')
print(f'Amentando 10%, temos {funcoes.aumento(valor, True)}')
