#Indica o novo salário de um funcionário com 15% de aumento.

sal = float(input('Qual é o salário do funcionário? R$'))
salf = sal + sal * (15 / 100)
print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, passa a receber R${salf:.2f}')
