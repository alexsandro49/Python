#Pergunta o sexo do usuário, 
# enquanto o sexo não é declarado, permanece em execução.

sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()[0]

while sexo not in 'FM':
    print('Dados inválidos.')
    sexo = str(input('Por favor, informe o seu sexo [F/M]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
