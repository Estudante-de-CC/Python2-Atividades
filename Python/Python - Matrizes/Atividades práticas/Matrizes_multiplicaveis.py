def dimensoes(matriz):
    linhas = 0
    colunas = 0
    for i in range(len(matriz)):
        linhas+=1
        colunas = len(matriz[i])

    return linhas, colunas

def sao_multiplicaveis(m1, m2):
    (l1, c1) = dimensoes(m1)
    (l2, c2) = dimensoes(m2)

    if c1 == l2:
        return True
    else:
        return False
