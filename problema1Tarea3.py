def sumaNaturales(lista, numero):
    
    tamanoLista = len(lista)
    memo = []
    for _ in range(tamanoLista + 1):
        memo.append([False] * (numero + 1)) #creacion memo matriz con puros False, de tamaño tamanoLista+1 x numero+1
    
    memo [0][0] = True #caso base, si no hay elementos en la lista, la suma es 0
    for i in range(1, tamanoLista+1): #recorrido horizontal de la matriz
        for j in range(numero+1): #recorrido vertical de la matriz
            memo[i][j] = memo[i-1][j] #se copia el valor de la fila anterior, principio backtracking
            if j >= lista[i-1] and memo[i-1][j-numero[i-1]]: #si el numero es mayor o igual al elemento de la lista y el valor de la fila anterior en la columna j-numero[i-1] es True
                
                memo[i][j] = True
    return memo[tamanoLista][numero]