#Calcula o valor de uma simulação de financiamento
#Caso a parcela > 30% do salário do comprador, o empréstimo é negado.

valor = float(input('Qual o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = valor / (anos * 12)

print(f'Para pegar uma casa de R${valor:.2f} em {anos} anos, a prestação será de {parcela:.2f}')

if parcela > salario * 0.3:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
