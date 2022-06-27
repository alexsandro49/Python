#Verifica se 3 segmentos podem formar um triângulo.

print('-='*20)
print('     Analisador de triângulos')
print('-='*20)

a1 = float(input('Primeiro segmento: '))
a2 = float(input('Segundo segmento: '))
a3 = float(input('Terceiro segmento: '))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmento não podem formar um triângulo!')
