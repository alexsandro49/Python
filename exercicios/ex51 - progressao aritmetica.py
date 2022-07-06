#Calcula os 10 primeiros termos de uma PA.

print('='*21)
print(' 10 TERMOS DE UMA PA ')
print('='*21)

termo0 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo0 + (10 -1) * razao

for c in range(termo0, decimo + razao, razao):
    print(c, end= ' ')
