#Calcula o custo de uma viagem, tendo base os km.
#R$0.50/km até 200km, acima disso, R$0.40/km

distancia = float(input('Qual é a distância da viagem? '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'Você está prestes a começar uma viagem de {distancia}km')
print(f'E o preço da sua passagem será de R${preco:.2f}!')
