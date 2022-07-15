#Lê dados para um cadastro de pessoas, mostra a número de cadastrados,
#além dos nomes das pessoas com o maior e o menorm, respectivamente.

lista = []
dados = []
pesagens = []
pessoas_max = []
pessoas_min = []
opcao = 'S'

print('=-='*15)
while True:
    if opcao in 'Nn':
        break
    nome = str(input('Nome: ')).strip()
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    lista.append(dados[:])
    pesagens.append(peso)
    dados.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] '))
        if opcao in 'Nn':
            break
        elif opcao in 'Ss':
            break
        else:
            print('Opção inválida.')
maior = max(pesagens)
menor = min(pesagens)
for p in lista:
    if maior in p:
        pessoas_max.append(p[0])
    if menor in p:
        pessoas_min.append(p[0])
print('=-='*15)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso cadastrado foi: {maior:.1f} . Peso de {pessoas_max}')
print(f'O menor peso cadastrado foi: {menor:.1f} . Peso de {pessoas_min}')
print('=-='*15)
