def subMaxima(matriz):

    num_filas, num_columnas = len(matriz), len(matriz[0])
    memo = []
    for _ in range(num_filas):
        memo.append([0] * num_columnas)     # Crear una matriz memo de tamaño num_filas x num_columnas inicializada con ceros
        
    # Variable para almacenar el tamaño máximo del subcuadro de 1s
    subMatrizMax = 0
    for i in range(num_filas):
        memo[i][0] = matriz[i][0]
        subMatrizMax = max(subMatrizMax, memo[i][0])
        
    for j in range(num_columnas):
        memo[0][j] = matriz[0][j]
        subMatrizMax = max(subMatrizMax, memo[0][j])
        
    for i in range(1, num_filas): # Llenar la matriz memo usando programación dinámica
        for j in range(1, num_columnas):
            if matriz[i][j] == 1:
                # Si el elemento actual es 1, calcular el tamaño del subcuadro de 1s
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
                # Actualizar el tamaño máximo del subcuadro de 1s
                subMatrizMax = max(subMatrizMax, memo[i][j])
    
    # Devolver el tamaño máximo del subcuadro de 1s encontrado
    return subMatrizMax