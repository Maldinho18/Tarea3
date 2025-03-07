def subMaxima(matriz):

    num_filas, num_columnas = len(matriz), len(matriz[0])
    memo = []
    for _ in range(num_filas):
        memo.append([0] * num_columnas)     
        
    
    subMatrizMax = 0
    for i in range(num_filas):
        memo[i][0] = matriz[i][0]
        subMatrizMax = max(subMatrizMax, memo[i][0])
        
    for j in range(num_columnas):
        memo[0][j] = matriz[0][j]
        subMatrizMax = max(subMatrizMax, memo[0][j])
        
    for i in range(1, num_filas): 
        for j in range(1, num_columnas):
            if matriz[i][j] == 1:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
                subMatrizMax = max(subMatrizMax, memo[i][j])
    
    return subMatrizMax