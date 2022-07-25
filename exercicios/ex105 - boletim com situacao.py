#Situação de boletim, com o total de dados,
#maior, menor, média e a situação atual (opcional).

def linha(msg):
    print('=-='*15)
    print(msg)
    print('=-='*15)
def notas(* n, sit = False):
    lista = {}
    lista['total'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['média'] = round(sum(n)/len(n), 2)
    if sit:
        if lista['média'] >= 7:
            lista['situação'] = 'BOA'
        if lista['média'] >= 5:
            lista['situação'] = 'RAZOÁVEL'
        if lista['média'] < 5:
            lista['situação'] = 'RUIM'
    return lista


resp = notas(5.5, 2.5, 10, 6.5, sit = True)
linha(resp)
