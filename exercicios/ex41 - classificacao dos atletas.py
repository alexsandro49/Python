#Mostra a classificação de um atleta, segundo a sua idade.
#Sempre usando o ano atual como base.

from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SENIOR'
else:
    categoria = 'MASTER'

print(f'O atleta tem {idade} anos')
print(f'Classificação: {categoria}')
