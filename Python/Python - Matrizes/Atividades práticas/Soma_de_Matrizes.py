def dimensoes(matriz):
    linhas = 0
    colunas = 0
    for i in range(len(matriz)):
        linhas+=1
        colunas = len(matriz[i])

    return linhas, colunas

def soma_matrizes(m1, m2):
    (i1, j1) = dimensoes(m1)
    (i2, j2) = dimensoes(m2)
    matriz = []
    if (i1, j1) == (i2, j2):
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[i])):
                linha.append(m1[i][j] + m2[i][j])
            matriz.append(linha)
        return matriz
    else:
        return False
                
                
