def subconjuntos(a, B):
    n = len(a)
    dp = [[False]*(B+1) for _ in range(n+1)]
    dp [0][0] = True
    for i in range(1, n+1):
        for j in range(B+1):
            dp[i][j] = dp[i-1][j]
            if j >= a[i-1] and dp[i-1][j-a[i-1]]:
                dp[i][j] = True
    return dp[n][B]