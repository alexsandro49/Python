#Converte uma medida indicada pelo usuário.

d = float(input('Digite uma distância em metros (m): '))
print(f'A medida de {d}m, corresponde a:')
print(f'{d/1000}km\n{d/100}hm\n{d/10}dam\n{d*10}dm\n{d*100}cm\n{d*1000}mm')
