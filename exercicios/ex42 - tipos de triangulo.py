#Verifica se há a existência de um triângulo, e diz seu tipo.

a1 = float(input('Primeiro segmento: '))
a2 = float(input('Segundo segmento: '))
a3 = float(input('Terceiro segmento: '))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Os segmentos podem formar um triângulo', end=' ')
    if a1 == a2 == a3:
        print('EQUILÁTERO!')
    elif a1 != a2 != a3 != a1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos não podem formar um triângulo!')
