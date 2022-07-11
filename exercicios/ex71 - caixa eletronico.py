#Caixa eletrônico com notas de R$50, R$20, R$10 e R$1.

print('='*27)
print('      BANCO DO CÓDIGO      ')
print('='*27)
dinheiro = int(input('Digite um valor para sacar: R$'))

total = dinheiro
valor = 50
cedulas = 0
while True:
    if total >= valor:
        total -= valor
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'{cedulas} notas de R${valor}')
        if valor == 50:
            valor = 20
        elif valor == 20:
            valor = 10
        elif valor == 10:
            valor = 1
        cedulas = 0
        if total == 0:
            break
