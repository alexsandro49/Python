#Calcula os gastos em uma loja, mostra o total gasto,
#quantos produtos custaram mais que R$1000 e qual foi o item mais barato.

print('=-'*15)
print('      LOJA SUPER GENÉRICA      ')
print('=-'*15)
soma = maior = menor = 0

while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    if soma == 0:
        menor = preco
    else:
        if preco > 1000:
            maior += 1
        if preco < menor:
            menor = preco
            nome = produto
    soma += preco
    continuar = str(input('Continuar [S/N]: ')).strip()
    if continuar in 'Nn':
        break
    if continuar in 'Ss':
        print('=-'*15)
print('=-'*15)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')
print('=-'*15)
