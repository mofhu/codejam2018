# author: mofhu@github
# 01 bag example

n = 4
wv = [
    (2,3),
    (1,2),
    (3,4),
    (2,2)
]
W = 5

dp = [[0 for i in range(n+10)] for j in range(W+10)]  # max n/w

# dp[i][j] -> weight <= w, max value
for i in range(n):
    for j in range(W+1):
        if j == 0:
            dp[i][j] = 0
        wi, vi = wv[i]
        if j >= wi:  # can add
            dp[i+1][j] = max(dp[i][j-wi] + vi, dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[n][W])

for i in range(n):
    print(i, dp[i])


