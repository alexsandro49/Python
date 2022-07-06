#Calcula o fatorial de um número.

fatorial = int(input('Digite um numero\n para calcular o seu fatorial: '))
contador = 1

print(f'Calculando {fatorial}! =', end=' ')
for c in range(fatorial, 0, -1):
    print(c, end=' ')
    if c > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')  
    contador *= c
print(contador)    
