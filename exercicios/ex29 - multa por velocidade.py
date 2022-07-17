#Pergunta a velocidade atual de um carro, caso esteja acima do limite, informa o valor da multa.
#limite: 80km/h || multa: R$7 km/h acima do limite.

velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa}!')

print('Tenha um bom dia! Dirija com segurança!')
