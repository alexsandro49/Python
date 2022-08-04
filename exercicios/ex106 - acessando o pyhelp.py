#Assistente para acessar o PyHELP, usando funções.

cores = ['\033[m', '\033[41m', '\033[0;42m', '\033[43m', 
         '\033[44m', '\033[45m', '\033[46m']

def ajuda(a):
    texto(f'Acessando o manual para... \'{a}\'',2)
    help(a)
def texto(msg, cor=0):
    print(cores[cor], end='')
    print('=' * (len(msg) + 4))
    print(f'  {msg}')
    print('=' * (len(msg) + 4))
    print(cores[0], end='')


texto('AJUDA PyHELP', 4)
while True:
    op = str(input('Digite uma função ou variável: '))
    if op.upper() == 'FIM':
        break
    else:
        ajuda(op)
texto('VOLTE SEMPRE!', 1)
