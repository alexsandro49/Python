def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo.\033[m')
    else:
        print(f'\033[33mArquivo {nome} criado com sucesso!\033[m')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[31mAconteceu um erro com o arquivo {nome}\033[m')
    else:
        print(a.read())
        a.close()