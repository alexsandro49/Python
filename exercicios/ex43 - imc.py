#Calcula o IMC do usuário com o peso e idade apresentadas.

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    faixa = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    faixa = 'PESO IDEAL'
elif 25 <= imc < 30:
    faixa = 'SOBREPESO'
elif 30 <= imc < 40:
    faixa = 'OBESIDADE'
else:
    faixa = 'OBESIDADE MORBIDA'

print(f'O IMC do usuário é de {imc:.2f}')
print(f'Você está na faixa de {faixa}!')
