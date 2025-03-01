def monedas(matrizMonedas):
    
    nFilas, nColumnas = len(matrizMonedas), len(matrizMonedas[0])
    memo = []
    for _ in range(nFilas):
        memo.append([0] * nColumnas)
        
    for j in range (nColumnas):
        memo[0][j] = matrizMonedas[0][j]
        
    for i in range(1, nFilas):
        for j in range(nColumnas):
            max_ = 0
            for k in [-1, 0, -1]:
                if 0 <= j + k < nColumnas:
                    max_ = max(max_, memo[i-1][j + k])
            memo[i][j] = matrizMonedas[i][j] + max_
            
    return max(memo[-1])