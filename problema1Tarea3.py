def sumaNaturales(lista, numero):
    
    tamanoLista = len(lista)
    memo = []
    for _ in range(tamanoLista + 1):
        memo.append([False] * (numero + 1)) 
    
    memo [0][0] = True 
    for i in range(1, tamanoLista+1): 
        for j in range(numero+1): 
            memo[i][j] = memo[i-1][j] 
            if j >= lista[i-1] and memo[i-1][j-numero[i-1]]: 
                
                memo[i][j] = True
    return memo[tamanoLista][numero]