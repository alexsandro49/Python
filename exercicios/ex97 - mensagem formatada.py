#Digita uma frase escolhida pelo usuário, formatada entre linhas.

def mensagem(msg):
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))

msg = str(input('Digite uma frase: ')).strip()
mensagem(msg)
