def dimensoes(matriz):
    linhas = 0
    colunas = 0
    for i in range(len(matriz)):
        linhas+=1
        colunas = len(matriz[i])

    print(str(linhas) + "X" + str(colunas) )