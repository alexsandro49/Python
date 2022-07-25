#Looping até que um número inteiro seja digitado.

def leiaInt(valor):
    while True:
        n = str(input(valor))
        if n.isnumeric():
            print(f'Você digitou o número: {n}')
            break
        else:
            print('ERRO! Digite um número válido.')


n = leiaInt('Digite um número inteiro: ')
