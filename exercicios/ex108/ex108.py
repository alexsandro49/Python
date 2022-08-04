#Mostra a metade, o dobro e um acréscimo de 10% de um número com formatado como moeda,
#usando funcoes em um arquivo separado para uma melhor organização.

import funcoes

valor = float(input('Digite um valor: '))
print(f'A metade de {funcoes.moeda(valor)} é {funcoes.moeda(funcoes.metade(valor))}')
print(f'O dobro de {funcoes.moeda(valor)} é {funcoes.moeda(funcoes.dobro(valor))}')
print(f'Amentando 10%, temos {funcoes.moeda(funcoes.aumento(valor))}')
