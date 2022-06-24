inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
c = 0
if inicio < fim:
    posi0 = inicio
    repet = fim - inicio
    numero = inicio
else:
    posi0 = fim
    repet = inicio - fim
    numero = fim

while c <= repet:
    print(f'{numero}..')
    c += 1
    numero += 1

