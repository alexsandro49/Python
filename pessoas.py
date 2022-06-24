continuar = 'S'
homens = 0
mulheres = 0

while continuar == 'S':
    print('=====================')
    print(' SELETOR DE PESSOAS  ')
    print('=====================')
    sexo = str(input('QUAL O SEXO? [M/F] : ')).upper()
    idade = int(input('QUAL A IDADE? : '))
    print('======================')
    print('QUAL A COR DO CABELO?')
    print('[1] - PRETO')
    print('[2] - CASTANHO')
    print('[3] - LOIRO')
    print('[4] - RUIVO')
    cabelo = int(input(': '))

    if sexo == 'M' and idade > 18 and cabelo == 2:
        homens += 1
    if sexo == 'F' and 25 <= idade <= 30 and cabelo == 3:
        mulheres += 1

    continuar = str(input('VOCÊ QUER CONTINUAR? [S/N] : ')).upper()

print('=====================')
print('   RESULTADO FINAL   ')
print('=====================')
print('O TOTAL DE PESSOAS HOMENS COM MAIS DE 18 ANOS')
print(f'E CABELOS CASTANHOS É {homens}')
print('O TOTAL DE MULHERES ENTRE 25 E 30 ANOS')
print(f'E CABELOS LOIROS É {mulheres}')
