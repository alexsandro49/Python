#Com algumas informações de uma pessoa, mostra seus dados e,
#caso tenha esteja trabalhando, mostra o tempo para se aposentar.

from datetime import date

dados = {}
ano = date.today().year
print('=-='*10)
dados['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano - nasc
dados['clts'] = int(input('Carteira de trabalho (0 - não): '))
if dados['clts'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - ano)
print('=-='*10)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}' )
print('=-='*10)
