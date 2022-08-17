#Menu de um sistema de cadastro de dados (parte 1).

from interface import opcoes

while True:
    a = opcoes.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if int(a) == 1:
        opcoes.lista()
    elif int(a) == 2:
        opcoes.novo()
    elif int(a) == 3:
        opcoes.sair()
