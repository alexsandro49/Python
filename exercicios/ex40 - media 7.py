#Calcula a media das notas, abaixo de 5 é reprovado
#entre 5-6.9 fica de recuperação e igual ou superior a 7 é aprovado.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print(f'Tirando {n1:.2f} e {n2:.2f}, a média do aluno é {media:.2f}')
if media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está em APROVADO.')
elif 7 > media >= 5:
    print('O aluno está RECUPERAÇÃO.')
