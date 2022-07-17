#Mostra uma frase com a data do nascimento do usuário.

dia = int(input('dia = '))
mes = str(input('mês = '))
ano = int(input('ano = '))

if mes == '1':
    mes = 'janeiro'
if mes == '2':
    mes = 'fevereiro'
if mes == '3':
    mes = 'março'
if mes == '4':
    mes = 'abril'
if mes == '5':
    mes = 'maio'
if mes == '6':
    mes = 'junho'
if mes == '7':
    mes = 'julho'
if mes == '8':
    mes = 'agosto'
if mes == '9':
    mes = 'setembro'
if mes == '10':
    mes = 'outubro'
if mes == '11':
    mes = 'novembro'
if mes == '12':
    mes = 'dezembro'
print(f'Você nasceu no dia {dia} de {mes} de {ano}, correto?')
