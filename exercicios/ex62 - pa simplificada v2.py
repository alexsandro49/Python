#Gera uma PA usando a função While, 
#com a quantidade de termos selecionada pelo usuário.

print('=-'*10)
print('   Gerador de PA   ')
print('=-'*10)
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('=-'*10)

c = 1
opcao = 1

while c < 11:
    print(f'{numero} ->', end=' ')
    numero += razao
    c += 1
print('PAUSA')
termos = 10
while opcao != 0:
    c = 1
    opcao = int(input('Mostrar quantos dos próximos termos: '))
    termos += opcao
    while c < opcao + 1:
        print(f'{numero} ->', end=' ')
        numero += razao
        c += 1
    if opcao != 0:
        print('PAUSA')
print(f'Progressão finalizada com {termos} termos.')
