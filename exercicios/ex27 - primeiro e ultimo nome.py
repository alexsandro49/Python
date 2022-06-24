#Primeiro e último nome.

nome = str(input('Digite o seu nome completo: ')).strip().split()
print('É um prazer em te conhecer!')
print('Seu primerio nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
