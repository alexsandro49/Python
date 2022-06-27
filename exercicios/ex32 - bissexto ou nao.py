#Informa se um ano é bissexto ou não.

ano = int(input('Que ano você quer analisar? 0 para ano atual: '))

if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')
