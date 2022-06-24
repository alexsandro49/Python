#Verifica se tem "Silva" no nome digitado.

nome = str(input('Qual é o seu nome completo? ')).strip().upper()
print('Seu nome tem Silva? {}.'.format('SILVA' in nome))
