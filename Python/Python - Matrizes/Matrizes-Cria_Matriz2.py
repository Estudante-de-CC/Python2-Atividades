def cria_matriz(lin, col, valor):
    matriz = []
    for i in range(lin):
        linha = []
        for j in range (col):
            linha.append(valor)

        matriz.append(linha)
    return matriz
