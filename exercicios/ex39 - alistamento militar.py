#Calcula quando foi/será o alistamento do usuário.

from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

print(f'Quem nasceu em {ano}, tem {idade} anos em 2022.')
if idade > 18:
    print(f'Voçê já deveria ter se alistado há {idade -18} anos!')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')

print(f'Seu alistamento foi em {2022 - (idade - 18)}.')
