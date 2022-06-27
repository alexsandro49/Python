#Calcula o custo de uma viagem, tendo base os km.
#km * 0.5 if viagem <= 200km else km * 0.45


distancia = float(input('Qual é a distância da viagem? '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'Você está prestes a começar uma viagem de {distancia}km')
print(f'E o preço da sua passagem será de R${preco:.2f}!')
