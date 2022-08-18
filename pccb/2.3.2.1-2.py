# author: mofhu@github
# complete bag problem
# 1-D array version

n = 3
wv = [
    (3,4),
    (4,5),
    (2,3),
]
W = 7

dp = [0 for i in range(W+10)]  # max n/w

# dp[i][j] -> weight <= j, max value
for i in range(n):
    for j in range(W+1):
        if j == 0:
            dp[j] = 0
        wi, vi = wv[i]
        if j >= wi:
            dp[j] = max(dp[j], dp[j-wi]+vi)
    print(dp)
print(dp[W])



