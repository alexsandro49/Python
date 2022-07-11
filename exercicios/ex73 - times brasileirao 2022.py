#Mostra a classificação do Brasileirão 2022, quem são os 5 primeiros times,
#os 4 últimos, os nomes em ordem alfábetica e a posição atual do Santos.

times = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Internacional',
         'São Paulo', 'Santos', 'Red Bull Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG',
         'Avaí', 'Ceará', 'Atlético-GO', 'Juventude', 'Fortaleza')

print('=-'*13)
print(f'Times do Brasileirão 2022: {times}')
print('=-'*13)
print(f'Os 5 primeiros são: {times[:5]}')
print('=-'*13)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-'*13)
print(f'Times em ordem alfábetica: {sorted(times)}')
print('=-'*13)
print(f'O Santos está na posição: {times.index("Santos")+1}')
print('=-'*13)
