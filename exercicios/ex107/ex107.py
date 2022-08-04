#Mostra a metade, o dobro e um acréscimo de 10% de um número,
#usando funcoes em outro arquivo para uma melhor organização.

import funcoes

valor = float(input('Digite um valor: '))
print(f'A metade de R${valor} é R${funcoes.metade(valor):.1f}')
print(f'O dobro de R${valor} é R${funcoes.dobro(valor):.1f}')
print(f'Amentando 10%, temos R${funcoes.aumento(valor):.1f}')
