#Menu de um sistema de cadastro de dados, conseguindo criar um arquivo
#e visualizar os dados pré-cadastrados (parte 2).

from arquivo import *
from interface import opcoes

arq = 'exercicios/ex115b/arquivo/teste01.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    a = opcoes.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if int(a) == 1:
        opcoes.lista()
        lerArquivo(arq)
    elif int(a) == 2:
        opcoes.novo()
    elif int(a) == 3:
        opcoes.sair()
