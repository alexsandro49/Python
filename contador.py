
resp = 4

while resp != 3:
    print('======================')
    print('|        MENU        |')
    print('======================')
    print('| [1] - De 1 até 10 |')
    print('| [2] - De 10 até 1 |')
    print('| [3] - Sair         ')
    resp = int(input(': '))

    if resp == 1:
        print('1.. 2.. 3.. 4.. 5.. 6.. 7.. 8.. 9.. 10..')
    if resp == 2:
        print('10.. 9.. 8.. 7.. 6.. 5.. 4.. 3.. 2.. 1..')
    if resp == 3:
        print('SAINDO...')
