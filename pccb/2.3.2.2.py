# author: mofhu@github
# 01 bag problem: variant

n = 4
wv = [
    (2,3),
    (1,2),
    (3,4),
    (2,2)
]
W = 5

v = len(wv)
maxn = 100
maxv = 100
dp = [[1000000000 for j in range(n*maxv+10)] for i in range(maxn+10)]
# dp: with n and sum vi, what is min W

# key is to iterate vi

dp[0][0] = 0
for i in range(n):
    for j in range(n*v+10):
        wi, vi = wv[i]
        if dp[i][j] + wi <= W:  # can add
            dp[i+1][j+vi] = min(dp[i][j] + wi, dp[i][j+vi])
            # print(wi, vi, dp[i+1][j+vi])
            dp[i+1][j] = dp[i][j]
        elif dp[i][j] <= W:
            dp[i+1][j] = dp[i][j]

# print(dp[n-1])
for i in range(n*v+10):
    if dp[n-1][i] <= W:
        ans = i

print(ans)

