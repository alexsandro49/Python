#Gera uma PA usando a função While.

print('=-'*10)
print('   Gerador de PA   ')
print('=-'*10)
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('=-'*10)
c = 1

print(f'{numero} ->', end=' ')
while c < 9:
    numero += razao
    print(f'{numero} ->', end=' ')
    c += 1
print('FIM')
