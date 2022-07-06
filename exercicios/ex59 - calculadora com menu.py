#Uma calculadora com várias operações, com um menu.

from time import sleep

valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
loop = True
while loop == True:
    print('     [1] - somar')
    print('     [2] - multiplicar')
    print('     [3] - maior')
    print('     [4] - novos números')
    print('     [0] - sair do programa')
    opcao = int(input('>>>>>>>>>>> Sua opção: '))
    
    if opcao == 1:
        print('=-'*15)
        print(f'A soma entre {valor1:.1f} + {valor2:.1f} é {valor1 + valor2:.1f}.')
        print('=-'*15)
    elif opcao == 2:
        print('=-'*15)
        print(f'A multiplicação entre {valor1:.1f} x {valor2:.1f} é {valor1 * valor2:.1f}.')
        print('=-'*15)
    elif opcao == 3:
        print('=-'*15)
        if valor1 > valor2:
            print(f'Entre {valor1:.1f} e {valor2:.1f}, o maior valor é {valor1:.1f}.')
        elif valor2 > valor1:
            print(f'Entre {valor1:.1f} e {valor2:.1f}, o maior valor é {valor2:.1f}.')
        elif valor1 == valor2:
            print(f'Entre {valor1:.1f} e {valor2:.1f}, os dois valores são iguais.')
        print('=-'*15)
    elif opcao == 4:
        print('=-'*15)
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
        print('=-'*15)
    elif opcao == 0:
        print('=-'*15)
        print('Finalizando.....')
        print('=-'*15)
        sleep(1)
        loop = False
    else:
        print('=-'*15)
        print('Opção inválida! Tente novamente.')
        print('=-'*15)
