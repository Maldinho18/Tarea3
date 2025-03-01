def subMaxima(mat):
    m, n = len(mat), len(mat[0])
    dp = [[0]*n for _ in range(m)]
    max_ = 0
    for i in range(m):
        dp[i][0] = mat[i][0]
        max_ = max(max_, dp[i][0])
    for j in range(n):
        dp[0][j] = mat[0][j]
        max_ = max(max_, dp[0][j])
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_ = max(max_, dp[i][j])
    return max_