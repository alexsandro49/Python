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
        for item in a:
            linha = item.split(';')
            linha[1] = linha[1].replace('\n', '')
            print(f'{linha[0]:<22}{linha[1]:>3} anos')
        a.close()

def escreverArquivo(nome, pessoa='vazio', idade=0):
    try:
        a = open(nome, 'at')
    except:
        print(f'\033[31mAconteceu um erro com o arquivo {nome}\033[m')
    else:
        try:
            a.write(f'{pessoa};{idade}\n')
        except:
            print('\033[31mHouve um erro na criação do arquivo\033[m')
        else:
            print(f'\033[33mO registro de {pessoa} foi adicionado!\033[m')
            a.close()

