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

dp = [[-1 for i in range(n+10)] for j in range(W+10)]

def rec(i, w):  # version 1: all in function, not preferred.
    print('iwv', i, w)
    if dp[i][w] >= 0:
        print('dp', i, w)
        return dp[i][w]
    if i == n:
        return 0
    wi, vi = wv[i]
    if w-wi >= 0:
        dp[i][w] = max(rec(i+1, w-wi)+vi, rec(i+1, w))
    else:
        dp[i][w] = rec(i+1, w)
    return dp[i][w]

print(rec(0, 5 ))
