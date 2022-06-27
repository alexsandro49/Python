#Calcula um aumento no salário.
#atual = +15% if antigo <= 1250 else atual = +10%

antigo = float(input('Qual é o salário do funcionário? R$'))

if antigo <= 1250:
    atual = antigo + (antigo*0.15)
else:
    atual = antigo + (antigo*0.1)

print(f'Quem ganhava R${antigo:.2f} passará a ganhar R${atual:.2f}')
