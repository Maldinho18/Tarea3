def monedas(grid):
    M, N = len(grid), len(grid[0])
    dp = [[0]*N for _ in range(M)]
    for j in range (N):
        dp[0][j] = grid[0][j]
    for i in range(1, M):
        for j in range(N):
            max_ = 0
            for k in [-1, 0, -1]:
                if 0 <= j + k < N:
                    max_ = max(max_, dp[i-1][j + k])
            dp[i][j] = grid[i][j] + max_
    return max(dp[-1])