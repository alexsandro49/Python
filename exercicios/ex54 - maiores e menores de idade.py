#Indica quantas pessoas são maiores de idades ou não, dentre 7.

from datetime import date

ano = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    p = int(input('Ano que a {}ª pessoa nasceu: '.format(c)))
    if ano - p >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também {menores} pessoas menores de idade')
