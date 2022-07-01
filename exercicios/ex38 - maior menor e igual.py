#Indica o maior valor entre dois números.

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

if primeiro > segundo:
    print(f'{primeiro} é maior que {segundo}')
elif segundo > primeiro:
    print(f'{segundo} é maior que {primeiro}')
else:
    print('Os dois valores são iguais.')
    