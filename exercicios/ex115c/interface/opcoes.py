def lista():
    print('='*30)
    print('{:^30}'.format('PESSOAS CADASTRADAS'))
    print('='*30)

def novo():
    print('='*30)
    print('{:^30}'.format('CADASTRAR PESSOA'))
    print('='*30)

def sair():
    print('='*30)
    print('{:^30}'.format('SAINDO DO SISTEMA...'))
    print('='*30)
    exit()

def menu(lista):
    while True:
        print('='*30)
        print('{:^30}'.format('MENU PRINCIPAL'))
        print('='*30)
        c = 1
        for item in lista:
            print(f'\033[34m{c} - {item}\033[m')
            c += 1
        print('='*30)
        while True:
            opcao = input('\033[32mSua opção: \033[m')
            if opcao.isalpha() or opcao == '':
                print('\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
            else:
                if opcao.isnumeric:
                    if int(opcao) >= 1 and int(opcao) <= len(lista):
                        break
                    else:
                        print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
        break
    return opcao
    
