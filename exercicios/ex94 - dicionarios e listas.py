#Análise de dados com pessoas cadastradas

pessoas = []
dados = {}
idade = 0

print('=-='*12)
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip()
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip()
    if dados['sexo'] not in 'MmFf':
        while True:
            print('Erro! Por favor, digite apenas M ou F.')
            dados['sexo'] = str(input('Sexo: [M/F] ')).strip()
            if dados['sexo'] in 'MmFf':
                break
    dados['idade'] = int(input('Idade: '))
    idade += dados['idade']
    pessoas.append(dados.copy())
    print('=-='*12)
    opcao = str(input('Deseja continuar? [S/N] ')).strip()
    if opcao not in 'SsNn':
        while True:
            print('Erro! Responda apenas S ou N.')
            opcao = str(input('Deseja continuar? [S/N] ')).strip()
            if opcao in 'SsNn':
                break
    if opcao in 'Nn':
        break

print('=-='*12)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {(idade / len(pessoas)):.1f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()
print('D) Lista de pessoas que estão acima da média')
for p in pessoas:
    if p['idade'] > idade / len(pessoas):
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"].upper()}; idade = {p["idade"]};')
print('=-='*12)
print('<< ENCERRADO >>')
