def dimensoes(matriz):
    linhas = 0
    colunas = 0
    for i in range(len(matriz)):
        linhas+=1
        colunas = len(matriz[i])

    return linhas, colunas

def imprime_matriz(matriz):
    '''  função imprime_matriz(matriz),
        que recebe uma matriz como parâmetro e
        imprime a matriz, linha por linha.'''

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(str(matriz[i][j]), end="")
            if (len(matriz[i])-1 != j):
                print(" ", end = "")
        print("")
