# author: mofhu@github
# LCS

n = 4
m = 4
s = 'abcd'
t = 'becd'

dp = [[0 for i in range(n+2)] for j in range(m+2)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(dp)
print(dp[n][m])
