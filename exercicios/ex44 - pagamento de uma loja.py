#Calcula as condições de pagamento de uma loja.
#Diferentes opções, custos variados.

print('=======LOJAS GUANABARA=======')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] - à vista dinheiro/cheque')
print('[2] - à vista cartão')
print('[3] - 2x no cartão')
print('[4] - 3x ou mais no cartão')
opcao = int(input('Sua opção: '))

if opcao == 1:
    final = preco - (preco*0.1)
    print(f'Sua compra de R${preco} vai custar R${final:.2f}.')
elif opcao == 2:
    final = preco - (preco*0.05)
    print(f'Sua compra de R${preco} vai custar R${final:.2f}.')
elif opcao == 3:
    final = preco
    mensal = preco / 2
    print(f'A compra parcelada em 2x de R${mensal:.2f}, sem juros.')
    print(f'Sua compra vai custar R${final:.2f}.')
elif opcao == 4:
    final = preco + (preco*0.2)
    parcelas = int(input('Número de parcelas: '))
    mensal = final / parcelas
    print(f'A compra parcelada em {parcelas}x de R${mensal:.2f}, com juros.')
    print(f'Sua compra de R${preco} vai custar R${final:.2f}.')
else:
    print('Opção inválida.')
