#Mostra o preço final de um produto com 5% de desconto.

preco = float(input('Qual o preço do produto? R$'))
precof = preco - preco * (5 / 100)
print(f'O produto que custava R${preco:.2f}, na promoção com 5% vai custar R${precof:.2f}')
