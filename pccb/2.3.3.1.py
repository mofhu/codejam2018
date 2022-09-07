# author: mofhu@github


n = 4
m = 3
M = 10000

MAX_M = m + 10
MAX_N = n + 10

dp = [[0 for i in range(MAX_M)] for j in range(MAX_N)]

dp[0][0] = 1
for i in range(1, m+1):
    for j in range(0, n+1):
        if j >= i:
            dp[i][j] = (dp[i][j-i] + dp[i-1][j]) % M
        else:
            dp[i][j] = dp[i-1][j]

print(dp)
print(dp[m][n])