#Indica quantos litros de tinta são necessários para pintar uma parede, seguindo suas medidas.
#Para cada 2m² é usado 1L de tinta (2m² == 1L).

l = float(input('Largura da parede (m): '))
a = float(input('Altura da parede (m): '))
area = l * a
tinta = area/2
print(f'Sua parede tem a dimensão de {l}m x {a}m e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
