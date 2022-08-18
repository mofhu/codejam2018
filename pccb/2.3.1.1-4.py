# author: mofhu@github
# 01 bag example
# recycle 1-D array

n = 4
wv = [
    (2,3),
    (1,2),
    (3,4),
    (2,2)
]
W = 5

dp = [0 for i in range(W+10)]  # max n/w

# dp[i][j] -> weight <= w, max value
for i in range(n-1):
    wi, vi = wv[i]
    for j in range(W, wi-1, -1):
        if j >= wi:  # can add
            dp[j] = max(dp[j-wi] + vi, dp[j])
    print(dp)
print(dp[W])

# print(dp)


