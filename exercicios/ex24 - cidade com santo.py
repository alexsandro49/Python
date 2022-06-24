#Diz se voce nasceu em uma cidade com "Santo" no nome.

cidade = str(input('Em que cidade você nasceu? ')).strip().upper()
print(cidade[:5] == 'SANTO')
