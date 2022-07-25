#Indica se é necessário votar, usando o ano de nascimento.

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO PRECISA VOTAR.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPTATIVO.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    

print('-'*35)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
print('-'*35)
