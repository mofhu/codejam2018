# author: mofhu@github
# complete bag problem

n = 3
wv = [
    (3,4),
    (4,5),
    (2,3),
]
W = 7

dp = [[0 for i in range(n+10)] for j in range(W+10)]  # max n/w

# dp[i][j] -> weight <= j, max value
for i in range(n):
    for j in range(W+1):
        if j == 0:
            dp[i][j] = 0
        wi, vi = wv[i]
        if j >= wi:
            while j >= wi:  # can add
                dp[i+1][j] = max(dp[i][j-wi] + vi, dp[i][j], dp[i+1][j-wi]+vi)
                j -= wi
        else:
            dp[i+1][j] = dp[i][j]
print(dp[n][W])

for i in range(n+1):
    print(i, dp[i])


