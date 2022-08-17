#Menu de um sistema de cadastro de dados, conseguindo criar um arquivo,
#visualizar seus dados e adicionar mais pessoas ao registro (parte 3).

from arquivo import *
from interface import opcoes

arq = 'exercicios/ex115c/arquivo/teste01.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    a = opcoes.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if int(a) == 1:
        opcoes.lista()
        lerArquivo(arq)
    elif int(a) == 2:
        opcoes.novo()
        nome = str(input('NOME: ')).strip()
        idade = int(input('IDADE: '))
        escreverArquivo(arq, nome, idade)
    elif int(a) == 3:
        opcoes.sair()
