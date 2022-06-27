#Diz se um número apresentado é IMPAR ou PAR.

numero = int(input('Me diga um número qualquer: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é IMPAR!')
