def soma(valores):
    """soma realiza a soma de dos valores de uma lista . retonar o  resultado da soma"""
    rs =0
    for i in  valores:
        rs +=i
    return rs


def media (valores):
    """media reliza soma dos valores divide os valore e divide pela quatidade de valores"""
    rs = 0 
    qtd = len(valores)
    for i in valores:
        rs +=i
    return rs/qtd

def maior (valores):
    """a  funçao  maior retorna o mair valor de uma lista"""
    m =valores[0]
    for i in valores:
        if i > m:
            m = i
    return m
"""a  funçao  menor retorna o menor valor de uma lista"""
def menor (valores):
    m = valores[0]
    for i in valores:
        if i < m:
            m = i
    return m