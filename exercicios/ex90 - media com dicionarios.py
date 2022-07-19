#Pede o nome e a nota do aluno, mostra os dados dele e sua situação atual.

dados = {}
print('=-='*10)
dados['nome'] = str(input('Nome: ')).strip()
dados['media'] =  float(input(f'Média do {dados["nome"]}: '))
if dados['media'] < 5:
    dados['situação'] = 'Reprovado'
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
if  5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
print('=-='*10)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
print('=-='*10)
