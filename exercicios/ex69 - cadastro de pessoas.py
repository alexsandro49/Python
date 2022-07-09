#Coleta dados num cadastro de pessoas. No final, mostra a quantidade de 
#adultos, homens cadastrados e mulheres com menos de 18 anos.

from ast import While

print('=-'*15)
print('      CADASTRO DE PESSOAS      ')
print('=-'*15)
pessoas = 1
homens = mulheres = adultos = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    print('=-'*15)
    if sexo in 'Mm':
        homens += 1
    if idade > 18:
        adultos += 1
    elif idade < 20 and sexo in 'Ff':
        mulheres += 1
    continuar = str(input('CONTINUAR? [S/N]: ')).strip()
    if continuar in 'Nn':
        print('=-'*15)
        break
    elif continuar in 'Ss':
        print('=-'*15)
        pessoas += 1

print(f'Total de pessoas com mais de 18 anos: {adultos}')
print(f'Ao todo, temos {homens} homens cadastrados')
print(f'E {mulheres} mulheres com menos de 20 anos.')
print('=-'*15)
