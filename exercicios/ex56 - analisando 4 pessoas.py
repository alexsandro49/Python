#Mostra dentre 4 pessoas, a média de idade, a idade e o nome do homem mais velho
#o número de mulheres com menos de 20 anos.

media = 0
velho = ''
mulheres = 0
maior = 0
for c in range(1,5):
    print(f'----- {c}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    if c == 1 and sexo == 'M':
        maior = idade
        velho = nome
    if idade > maior and sexo == 'M':
        maior = idade
        velho = nome
    if idade < 20 and sexo == 'F':
        mulheres += 1

print(f'A média de idade do grupo é de {media / 4:.1f} anos.')
if velho != '':
    print(f'O homem mais velho tem {maior} anos e se chama {velho}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
