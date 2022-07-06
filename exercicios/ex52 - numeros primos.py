#Testa se um número é primo, mostrando as situações em que ele é divisível.

n = int(input('Digite um número: '))
vezes = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        vezes += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível por {vezes} vezes')

if vezes > 2:
    print('Por isso ele NÃO É PRIMO!')
else:
    print('Por isso ele É PRIMO!')
